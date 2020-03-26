from .base_sensor import BaseSensor
from typing import Dict
from busio import I2C
import adafruit_bme680
from misc.units import Temp
import time
from misc.config import Config


class BME680(BaseSensor):

    def __init__(self, i2c: I2C, config: Config):
        super().__init__(self.__class__.__name__, config)
        self.i2c = i2c
        self.sensor = adafruit_bme680.Adafruit_BME680_I2C(self.i2c)
        self.sensor.sea_level_pressure = self.config.pressure

    def calibrate(self, iterations: int):
        for x in range(iterations):
            self.sensor.temperature
            self.sensor.gas
            self.sensor.pressure
            self.sensor.altitude

    def debug(self):
        self.logger.info(f"Temperature: {self.temp.normalize(self.sensor.temperature)} {self.temp}")
        self.logger.info(f"VOC: {self.sensor.gas} ohm")
        self.logger.info(f"Humidity: {self.sensor.humidity} %")
        self.logger.info(f"Pressure: {self.sensor.pressure} hPa")
        self.logger.info(f"Altitude: {self.sensor.altitude} meters")

    def read(self) -> Dict:
        timestamp = time.time_ns()
        return [
                {
                    "measurement": "temperature",
                    "tags": {
                        "location": self.location.to_string(),
                        "sensor": self.name,
                        "reading": "temperature"
                        },
                    "time": timestamp,
                    "fields": {
                        "value": self.temp.normalize(self.sensor.temperature)
                        }
                    },
                {
                    "measurement": "voc",
                    "tags": {
                        "location": self.location.to_string(),
                        "sensor": self.name,
                        "reading": "voc"
                        },
                    "time": timestamp,
                    "fields": {
                        "value": self.sensor.gas
                        }
                    },
                {
                    "measurement": "humidity",
                    "tags": {
                        "location": self.location.to_string(),
                        "sensor": self.name,
                        "reading": "humidity"
                        },
                    "time": timestamp,
                    "fields": {
                        "value": self.sensor.humidity
                        }
                    },
                {
                    "measurement": "pressure",
                    "tags": {
                        "location": self.location.to_string(),
                        "sensor": self.name,
                        "reading": "pressure"
                        },
                    "time": timestamp,
                    "fields": {
                        "value": self.sensor.pressure
                        }
                    }
                ]

