from __future__ import annotations
import threading
from PyQt6 import QtWidgets, QtCore

import mainwindow
import configwindow
import beeper
import config
import data
import mqtt


class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])

        self.config = config.Config()

        self.sensor = data.SensorData(self)
        self.timer = data.TimerData(self)
        self.mqtt = mqtt.MQTTListener(self)
        self.beeper = beeper.Beeper()

        self.m_window = mainwindow.MainWindow(self)
        self.m_window.show()

        self.c_window = configwindow.ConfigWindow(self)

        self.thread_beeper = threading.Thread(target=self.beeper.start, args=(), daemon=True)
        self.thread_beeper.start()

    def close_app(self):
        self.mqtt.stop()


