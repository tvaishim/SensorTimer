import configparser

import logger


INI_FILE = r"config.ini"


class Config:
    def __init__(self):
        self.data_config = configparser.ConfigParser(delimiters="=")
        self.load_config()

        try:
            self.mqtt_server = self.data_config.get('MQTT', 'server')
        except Exception as e:
            self.mqtt_server = ""
            logger.logger.error("Ошибка чтения файла настроек - параметр <[MQTT] Server>")

        try:
            self.mqtt_port = self.data_config.getint('MQTT', 'port')
        except Exception as e:
            self.mqtt_port = 1883
            logger.logger.error("Ошибка чтения файла настроек - параметр <[MQTT] Port>")

        try:
            self.mqtt_user = self.data_config.get('MQTT', 'user')
        except Exception as e:
            self.mqtt_user = ""
            logger.logger.error("Ошибка чтения файла настроек - параметр <[MQTT] User>")

        try:
            self.mqtt_password = self.data_config.get('MQTT', 'password')
        except Exception as e:
            self.mqtt_password = ""
            logger.logger.error("Ошибка чтения файла настроек - параметр <[MQTT] Password>")

        try:
            self.mqtt_topic = self.data_config.get('MQTT', 'topic')
        except Exception as e:
            self.mqtt_topic = ""
            logger.logger.error("Ошибка чтения файла настроек - параметр <[MQTT] Topic>")

        try:
            self.mqtt_expire = self.data_config.getint('MQTT', 'expire')
        except Exception as e:
            self.mqtt_expire = 60
            logger.logger.error("Ошибка чтения файла настроек - параметр <[MQTT] Expire>")

        try:
            self.sensor_max = self.data_config.getint('SENSOR', 'max')
        except Exception as e:
            self.sensor_max = 100
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SENSOR] max>")

        try:
            self.sensor_min = self.data_config.getint('SENSOR', 'min')
        except Exception as e:
            self.sensor_min = 0
            logger.logger.error("Ошибка чтения файла настроек - параметр <[SENSOR] min>")

    def load_config(self):
        self.data_config.read(INI_FILE)

    def save_config(self):
        self.data_config['MQTT'] = {
            'server': self.mqtt_server,
            'port': str(self.mqtt_port),
            'user': self.mqtt_user,
            'password': self.mqtt_password,
            'topic': self.mqtt_topic,
            'expire': self.mqtt_expire,
        }
        self.data_config['SENSOR'] = {
            'max': str(self.sensor_max),
            'min': str(self.sensor_min),
        }
        with open(INI_FILE, 'w') as config_file:
            self.data_config.write(config_file)

