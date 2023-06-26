from __future__ import annotations
from PyQt6 import QtWidgets, QtGui

import mainapp
import configform


class ConfigWindow(QtWidgets.QDialog):
    def __init__(self, parent: mainapp.App):
        super().__init__()

        self.app = parent

        self.ui = configform.Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Config")
        self.setFixedSize(self.width(), self.height())

        self.ui.mqttPort.setValidator(QtGui.QIntValidator(1000, 65535))
        self.ui.mqttExpire.setValidator(QtGui.QIntValidator(0, 9999))

        self.ui.btnOK.pressed.connect(self.button_ok)
        self.ui.btnCancel.pressed.connect(self.button_cancel)

    def button_ok(self):
        self.app.config.mqtt_server = self.ui.mqttServer.text()
        self.app.config.mqtt_port = int(self.ui.mqttPort.text())
        self.app.config.mqtt_user = self.ui.mqttUser.text()
        self.app.config.mqtt_password = self.ui.mqttPassword.text()
        self.app.config.mqtt_topic = self.ui.mqttTopic.text()
        self.app.config.mqtt_expire = int(self.ui.mqttExpire.text())
        self.app.config.save_config()
        self.close()

    def button_cancel(self):
        self.close()

    def load_config(self):
        self.ui.mqttServer.setText(self.app.config.mqtt_server)
        self.ui.mqttPort.setText(str(self.app.config.mqtt_port))
        self.ui.mqttUser.setText(self.app.config.mqtt_user)
        self.ui.mqttPassword.setText(self.app.config.mqtt_password)
        self.ui.mqttTopic.setText(self.app.config.mqtt_topic)
        self.ui.mqttExpire.setText(str(self.app.config.mqtt_expire))

    def showEvent(self, _):
        self.load_config()
