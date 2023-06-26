from __future__ import annotations
import enum
import time

import mainapp
import logger


class TimerType(enum.Enum):
    clock = 1
    timer = 2
    countdown = 3


class TimerData:
    def __init__(self, parent: mainapp.App):
        self.__app = parent
        self.__type = TimerType.clock
        self.__value = time.time()
        self.__start_time = 0
        self.__end_time = 0
        self.__alarm = False
        self.__warning = False

    def __set_warning(self):
        self.__warning = (self.__type != TimerType.clock) and (self.__value >= self.__end_time)

    @property
    def value(self):
        self.__value = time.time()
        return self.__value

    @property
    def alarm(self):
        _ = self.value
        self.__set_warning()
        return self.__alarm, self.__warning

    @staticmethod
    def str_to_time(value: str):
        value = value.replace(" ", "")
        try:
            match value.count(":"):
                case 2:
                    t = time.strptime(value, "%H:%M:%S")
                case 1:
                    t = time.strptime(value, "%H:%M")
                case 0:
                    t = time.strptime(value, "%M")
                case _:
                    t = time.strptime("0", "%M")
        except ValueError:
            t = time.strptime("0", "%M")

        return t.tm_hour, t.tm_min, t.tm_sec

    @staticmethod
    def add_time(s_time, th, tm, ts):
        st_time = time.localtime(s_time)
        str_time = f"{st_time.tm_year}{st_time.tm_mon}{st_time.tm_mday}{th}{tm}{ts}"
        return time.mktime(time.strptime(str_time, "%Y%m%d%H%M%S"))

    def timer_set(self, value_timer, value_cd: str):

        t_hour, t_min, t_sec = TimerData.str_to_time(value_timer)
        if t_hour or t_min or t_sec:
            t_now = time.time()
            t = TimerData.add_time(t_now, t_hour, t_min, t_sec)
            if t < t_now:
                t += 86400

            self.__type = TimerType.timer
            self.__start_time = t_now
            self.__end_time = t
            self.__alarm = True
            return

        t_hour, t_min, t_sec = TimerData.str_to_time(value_cd)
        if t_hour or t_min or t_sec:
            t_now = time.time()
            t = t_now + t_hour * 3600 + t_min * 60 + t_sec

            self.__type = TimerType.countdown
            self.__start_time = t_now
            self.__end_time = t
            self.__alarm = True
            return

        self.__type = TimerType.clock

    def timer_off(self):
        self.__type = TimerType.clock
        self.__alarm = False
        self.__warning = False

    def __repr__(self):
        value = self.value
        return f"Value: {value}, {time.strftime('%H:%M:%S', time.localtime(value))}"

    def __str__(self):
        value = self.value
        match self.__type:
            case TimerType.clock:
                return time.strftime('%H:%M:%S', time.localtime(value))
            case TimerType.timer:
                return time.strftime('%H:%M:%S', time.localtime(value))
            case TimerType.countdown:
                ost_t = max(self.__end_time - value, 0)
                return time.strftime('%H:%M:%S', time.gmtime(ost_t))


class SensorData:

    def __init__(self, parent: mainapp.App):
        self.__app = parent
        self.__actual = False
        self.__value = 0.0
        self.__last_update = 0
        self.__alarm = False
        self.__warning = False
        self.__min_value = self.__app.config.sensor_min
        self.__max_value = self.__app.config.sensor_max

    def __set_actuality(self):
        self.__actual = (time.time() - self.__last_update) <= self.__app.config.mqtt_expire

    def __set_warning(self):
        self.__warning = not (self.__min_value <= self.__value <= self.__max_value) and self.__actual and self.__alarm

    @property
    def value(self):
        self.__set_actuality()
        return self.__value, self.__actual

    @value.setter
    def value(self, value):
        self.__value = value
        self.__last_update = time.time()

    @property
    def alarm(self):
        self.__set_actuality()
        self.__set_warning()
        return self.__alarm, self.__warning

    @alarm.setter
    def alarm(self, value):
        self.__alarm = value

    def alarm_set(self, min_value: int, max_value: int):
        self.__min_value = min_value
        self.__max_value = max_value

    def __repr__(self):
        value, actual = self.value
        return f"Value: {value}, Actual: {actual}"

    def __str__(self):
        value, actual = self.value
        if actual:
            return f"{value:4.1f}"
        else:
            return "---"


