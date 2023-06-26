from __future__ import annotations
from PyQt6 import QtWidgets, QtCore

import mainapp
import mainform
import logger
import mqtt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent: mainapp.App):
        super().__init__()

        self.app = parent

        self.ui = mainform.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Timer")
        self.setFixedSize(self.width(), self.height())

        self.ui.btnMQTT.pressed.connect(self.btn_mqtt_pressed)
        self.ui.btnConfig.pressed.connect(self.btn_config_pressed)

        self.ui.scrSensor.mouseDoubleClickEvent = self.sensor_click
        self.ui.scrTimer.mouseDoubleClickEvent = self.timer_click

        self.ui.editSMax.editingFinished.connect(self.edit_smax_changed)
        self.ui.editSMin.editingFinished.connect(self.edit_smin_changed)

        self.form_repaint()

        # Таймер обновления экрана
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.form_repaint)
        self.timer.start(250)

    def btn_mqtt_pressed(self):
        match self.app.mqtt.status:
            case mqtt.MQTTStatus.off:
                self.app.mqtt.start()
            case mqtt.MQTTStatus.on:
                self.app.mqtt.stop()

    def sensor_click(self, event):
        self.ui.scrSensor.setFocus()
        alarm, warning = self.app.sensor.alarm
        self.app.sensor.alarm = not alarm

    def btn_config_pressed(self):
        self.app.c_window.exec()

    def timer_click(self, event):
        self.ui.scrTimer.setFocus()
        alarm, warning = self.app.timer.alarm
        if alarm:
            self.app.timer.timer_off()
        else:
            self.app.timer.timer_set(self.ui.editTimer.text(), self.ui.editCD.text())

    def edit_smax_changed(self):
        self.app.sensor.alarm_set(int(self.ui.editSMin.text()), int(self.ui.editSMax.text()))

    def edit_smin_changed(self):
        self.app.sensor.alarm_set(int(self.ui.editSMin.text()), int(self.ui.editSMax.text()))

    def form_repaint(self):
        match self.app.mqtt.status:
            case mqtt.MQTTStatus.connection:
                self.ui.btnMQTT.setStyleSheet("background-color: #F0F000;")
            case mqtt.MQTTStatus.on:
                self.ui.btnMQTT.setStyleSheet("background-color: #00F000;")
            case _:
                self.ui.btnMQTT.setStyleSheet("background-color: #F0F0F0;")

        self.ui.scrSensor.setText(str(self.app.sensor))

        s_alarm, s_warning = self.app.sensor.alarm
        if s_warning:
            self.ui.scrSensor.setStyleSheet("color: #FF0000; background-color: #FFFFFF;")
        else:
            if s_alarm:
                self.ui.scrSensor.setStyleSheet("color: #007F00; background-color: #FFFFFF;")
            else:
                self.ui.scrSensor.setStyleSheet("color: #000000; background-color: #FFFFFF;")

        self.ui.scrTimer.setText(str(self.app.timer))

        t_alarm, t_warning = self.app.timer.alarm
        if t_warning:
            self.ui.scrTimer.setStyleSheet("color: #FF0000; background-color: #FFFFFF;")
        else:
            if t_alarm:
                self.ui.scrTimer.setStyleSheet("color: #007F00; background-color: #FFFFFF;")
            else:
                self.ui.scrTimer.setStyleSheet("color: #000000; background-color: #FFFFFF;")

        self.app.beeper.alarm = s_warning or t_warning

    #     self.sensors = sensors.sensors
    #     self.form_repaint()
    #     self.btn_2_pressed()
    #
    #     # Таймер обновления экрана
    #     self.timer = QtCore.QTimer()
    #     self.timer.timeout.connect(self.form_repaint)
    #     self.timer.start(1000)
    #
    #     self.ui.lbl_snsr_1.mouseDoubleClickEvent = self.lbl_snsr_1_dbl_click
    #     self.ui.lbl_snsr_2.mouseDoubleClickEvent = self.lbl_snsr_2_dbl_click
    #     self.ui.lbl_snsr_3.mouseDoubleClickEvent = self.lbl_snsr_3_dbl_click
    #     self.ui.lbl_snsr_4.mouseDoubleClickEvent = self.lbl_snsr_4_dbl_click
    #     self.ui.lbl_snsr_5.mouseDoubleClickEvent = self.lbl_snsr_5_dbl_click
    #     self.ui.lbl_snsr_6.mouseDoubleClickEvent = self.lbl_snsr_6_dbl_click
    #
    #     self.ui.btn_1_connect.pressed.connect(self.btn_1_pressed)
    #     self.ui.btn_2.pressed.connect(self.btn_2_pressed)

    #     self.ui.btn_mqtt.pressed.connect(self.btn_mqtt_pressed)
    #
    # def btn_1_pressed(self):
    #     if comport.com.comport.is_open:
    #         comport.com.close_port()
    #     else:
    #         if self.ui.cbx_1_comports.currentIndex() >= 0:
    #             comport.com.comport.port = self.ui.cbx_1_comports.currentText()
    #             comport.com.open_port()
    #
    # def btn_mqtt_pressed(self):
    #     mqtt.mqttSender.is_active = not mqtt.mqttSender.is_active
    #
    # def btn_2_pressed(self):
    #     ports = comport.com.list_serial_ports()
    #     self.ui.cbx_1_comports.clear()
    #     self.ui.cbx_1_comports.addItems(ports)
    #     if comport.com.comport.port in ports:
    #         self.ui.cbx_1_comports.setCurrentText(comport.com.comport.port)
    #
    # def lbl_snsr_1_dbl_click(self, event):
    #     self.sensors.sensors[1].alarm = not self.sensors.sensors[1].alarm
    #
    # def lbl_snsr_2_dbl_click(self, event):
    #     self.sensors.sensors[2].alarm = not self.sensors.sensors[2].alarm
    #
    # def lbl_snsr_3_dbl_click(self, event):
    #     self.sensors.sensors[3].alarm = not self.sensors.sensors[3].alarm
    #
    # def lbl_snsr_4_dbl_click(self, event):
    #     self.sensors.sensors[4].alarm = not self.sensors.sensors[4].alarm
    #
    # def lbl_snsr_5_dbl_click(self, event):
    #     self.sensors.sensors[5].alarm = not self.sensors.sensors[5].alarm
    #
    # def lbl_snsr_6_dbl_click(self, event):
    #     self.sensors.sensors[6].alarm = not self.sensors.sensors[6].alarm



    # def form_repaint(self):
    #     if self.sensors.start_time:
    #         work_time = int(time.time()) - self.sensors.start_time
    #         work_time_hour = work_time // 3600
    #         work_time = work_time % 3600
    #         work_time_min = work_time // 60
    #         self.ui.lbl_time.setText(f"{work_time_hour:02}:{work_time_min:02}")
    #     else:
    #         # work_time = int(time.time())
    #         # work_time_min = work_time % 60
    #         # self.ui.lbl_time.setText(f"00:{work_time_min:02}")
    #         self.ui.lbl_time.setText("--:--")
    #
    #     if self.sensors.start_time:
    #         work_time = int(self.sensors.sensors[0].value) - self.sensors.start_wtime
    #         work_time_hour = work_time // 3600
    #         work_time = work_time % 3600
    #         work_time_min = work_time // 60
    #         self.ui.lbl_snsr_0.setText(f"{work_time_hour:02}:{work_time_min:02}")
    #     else:
    #         self.ui.lbl_snsr_0.setText("--:--")
    #
    #     self.ui.lbl_snsr_1.setText(format(self.sensors.sensors[1].value, f".{self.sensors.sensors[1].round}f"))
    #     self.ui.lbl_snsr_2.setText(format(self.sensors.sensors[2].value, f".{self.sensors.sensors[2].round}f"))
    #     self.ui.lbl_snsr_3.setText(format(self.sensors.sensors[3].value, f".{self.sensors.sensors[3].round}f"))
    #     self.ui.lbl_snsr_4.setText(format(self.sensors.sensors[4].value, f".{self.sensors.sensors[4].round}f"))
    #     self.ui.lbl_snsr_5.setText(format(self.sensors.sensors[5].value, f".{self.sensors.sensors[5].round}f"))
    #     self.ui.lbl_snsr_6.setText(format(self.sensors.sensors[6].value, f".{self.sensors.sensors[6].round}f"))
    #
    #     if self.sensors.sensors[1].is_alarm():
    #         self.ui.lbl_snsr_1.setStyleSheet(styles.lbl_sensor_warning)
    #     elif self.sensors.sensors[1].alarm:
    #         self.ui.lbl_snsr_1.setStyleSheet(styles.lbl_sensor_ok)
    #     else:
    #         self.ui.lbl_snsr_1.setStyleSheet(styles.lbl_sensor_not_alarm)
    #
    #     if self.sensors.sensors[2].is_alarm():
    #         self.ui.lbl_snsr_2.setStyleSheet(styles.lbl_sensor_warning)
    #     elif self.sensors.sensors[2].alarm:
    #         self.ui.lbl_snsr_2.setStyleSheet(styles.lbl_sensor_ok)
    #     else:
    #         self.ui.lbl_snsr_2.setStyleSheet(styles.lbl_sensor_not_alarm)
    #
    #     if self.sensors.sensors[3].is_alarm():
    #         self.ui.lbl_snsr_3.setStyleSheet(styles.lbl_sensor_warning)
    #     elif self.sensors.sensors[3].alarm:
    #         self.ui.lbl_snsr_3.setStyleSheet(styles.lbl_sensor_ok)
    #     else:
    #         self.ui.lbl_snsr_3.setStyleSheet(styles.lbl_sensor_not_alarm)
    #
    #     if self.sensors.sensors[4].is_alarm():
    #         self.ui.lbl_snsr_4.setStyleSheet(styles.lbl_sensor_warning)
    #     elif self.sensors.sensors[4].alarm:
    #         self.ui.lbl_snsr_4.setStyleSheet(styles.lbl_sensor_ok)
    #     else:
    #         self.ui.lbl_snsr_4.setStyleSheet(styles.lbl_sensor_not_alarm)
    #
    #     if self.sensors.sensors[5].is_alarm():
    #         self.ui.lbl_snsr_5.setStyleSheet(styles.lbl_sensor_warning)
    #     elif self.sensors.sensors[5].alarm:
    #         self.ui.lbl_snsr_5.setStyleSheet(styles.lbl_sensor_ok)
    #     else:
    #         self.ui.lbl_snsr_5.setStyleSheet(styles.lbl_sensor_not_alarm)
    #
    #     if self.sensors.sensors[6].is_alarm():
    #         self.ui.lbl_snsr_6.setStyleSheet(styles.lbl_sensor_warning)
    #     elif self.sensors.sensors[6].alarm:
    #         self.ui.lbl_snsr_6.setStyleSheet(styles.lbl_sensor_ok)
    #     else:
    #         self.ui.lbl_snsr_6.setStyleSheet(styles.lbl_sensor_not_alarm)
    #
    #     if comport.com.comport.is_open:
    #         self.ui.btn_1_connect.setStyleSheet("background-color: #00F000;")
    #     else:
    #         self.ui.btn_1_connect.setStyleSheet("background-color: #F0F0F0;")
    #
    #     if mqtt.mqttSender.is_active:
    #         self.ui.btn_mqtt.setStyleSheet("background-color: #00F000;")
    #     else:
    #         self.ui.btn_mqtt.setStyleSheet("background-color: #F0F0F0;")
    #
    #     if comport.com.comport.is_open:
    #         beeper.beeper.alarm = self.sensors.sensors[1].is_alarm() or \
    #                               self.sensors.sensors[2].is_alarm() or \
    #                               self.sensors.sensors[3].is_alarm() or \
    #                               self.sensors.sensors[4].is_alarm() or \
    #                               self.sensors.sensors[5].is_alarm() or \
    #                               self.sensors.sensors[6].is_alarm()

    def closeEvent(self, event):
        self.app.config.sensor_max = int(self.ui.editSMax.text())
        self.app.config.sensor_min = int(self.ui.editSMin.text())
        self.app.config.save_config()
        self.app.close_app()
