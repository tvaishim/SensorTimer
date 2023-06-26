import winsound
import time


class Beeper:
    def __init__(self):
        self.__alarm = False

    def start(self):
        while True:
            if self.__alarm:
                winsound.Beep(2000, 1000)
            time.sleep(0.5)

    @property
    def alarm(self):
        return self.__alarm

    @alarm.setter
    def alarm(self, value):
        self.__alarm = value

