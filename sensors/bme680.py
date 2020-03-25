from .base_sensor import BaseSensor
from typing import Dict
from busio import I2C
import adafruit_bme680
from misc.units import Temp
import time


class BME680(BaseSensor):

    def __init__(self, i2c: I2C, temp: Temp = Temp.CELSIUS, pressure: float=760.0, loc: str = "living_room"):
        super().__init__(self.__class__.__name__, temp, loc)
        self.i2c = i2c
        self.sensor = adafruit_bme680.Adafruit_BME680_I2C(self.i2c)
        self.sensor.sea_level_pressure = pressure

    def calibrate(self, iterations: int):
        for x in range(iterations):
            self.sensor.temperature
            self.sensor.gas
            self.sensor.pressure
            self.sensor.altitude

    def debug(self):
        self.logger.info(f"Temperature: {self.temp.normalize(self.sensor.temperature)} {self.temp}")
        self.logger.info(f"Gas: {self.sensor.gas} ohm")
        self.logger.info(f"Humidity: {self.sensor.humidity} %")
        self.logger.info(f"Pressure: {self.sensor.pressure} hPa")
        self.logger.info(f"Altitude: {self.sensor.altitude} meters")

    def read(self) -> Dict:
        timestamp = time.time_ns()
        return [
                {
                    "measurement": "temperature",
                    "tags": {
                        "location": self.location,
                        "sensor": self.name,
                        "reading": "temperature"
                        },
                    "time": timestamp,
                    "fields": {
                        "temp": self.temp.normalize(self.sensor.temperature)
                        }
                    },
                {
                    "measurement": "gas",
                    "tags": {
                        "location": self.location,
                        "sensor": self.name,
                        "reading": "gas"
                        },
                    "time": timestamp,
                    "fields": {
                        "ohms": self.sensor.gas
                        }
                    },
                {
                    "measurement": "humidity",
                    "tags": {
                        "location": self.location,
                        "sensor": self.name,
                        "reading": "humidity"
                        },
                    "time": timestamp,
                    "fields": {
                        "humidity": self.sensor.humidity
                        }
                    },
                {
                    "measurement": "pressure",
                    "tags": {
                        "location": self.location,
                        "sensor": self.name,
                        "reading": "pressure"
                        },
                    "time": timestamp,
                    "fields": {
                        "pressure": self.sensor.pressure
                        }
                    }
                ]

