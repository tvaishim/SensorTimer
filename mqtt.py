from __future__ import annotations
import enum
import paho.mqtt.client as mqtt

import mainapp
import logger


class MQTTStatus(enum.Enum):
    off = 0
    connection = 1
    on = 2


class MQTTListener:
    def __init__(self, parent: mainapp.App):
        self.__app = parent
        self.__status = MQTTStatus.off
        self.__first_message = True
        self.__client = mqtt.Client()
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message
        self.__client.on_disconnect = self.__on_disconnect
        self.__client.username_pw_set(self.__app.config.mqtt_user, self.__app.config.mqtt_password)

    def __on_connect(self, client, userdata, flags, rc):
        if rc:
            logger.logger.error("Ошибка подключения к MQTT серверу. Код ошибки " + str(rc))
        else:
            logger.logger.debug("MQTT connected")
            client.subscribe(self.__app.config.mqtt_topic)
            self.__status = MQTTStatus.on

    def __on_message(self, client, userdata, msg):
        logger.logger.debug(f"MQTT message: {msg.topic} - {str(msg.payload)}")
        if self.__first_message:
            logger.logger.debug("first message")
            self.__first_message = False
            return
        self.__app.sensor.value = float(msg.payload)

    def __on_disconnect(self, client, userdata, rc):
        if rc:
            logger.logger.error("Ошибка отключения от MQTT сервера. Код ошибки " + str(rc))
        else:
            logger.logger.debug("MQTT disconnected")
            self.__status = MQTTStatus.off

    @property
    def status(self):
        return self.__status

    def start(self):
        if self.__status == MQTTStatus.off:
            self.__status = MQTTStatus.connection
            self.__first_message = True
            self.__client.connect(self.__app.config.mqtt_server, self.__app.config.mqtt_port, 60)
            self.__client.loop_start()

    def stop(self):
        if self.__status == MQTTStatus.on:
            self.__status = MQTTStatus.connection
            self.__client.loop_stop()
            self.__client.disconnect()
