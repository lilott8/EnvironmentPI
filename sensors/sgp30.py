from .base_sensor import BaseSensor
from typing import Dict
from misc.units import Temp
import adafruit_sgp30
from busio import I2C
import time
from misc.config import Config


class SGP30(BaseSensor):

    def __init__(self, i2c: I2C, config: Config):
        super().__init__(self.__class__.__name__, config)
        try:
            self.sensor = adafruit_sgp30.Adafruit_SGP30(i2c)
            self.sensor.iaq_init()
            self.sensor.set_iaq_baseline(0x8973, 0x8AAE)
            self.enabled = True
        except:
            self.enabled = False

    def calibrate(self, iterations: int):
        if self.enabled:
            for x in range(iterations):
                self.sensor.eCO2
                self.sensor.TVOC
            self.logger.info("Done calibrating SGP30")
        else:
            self.logger.error("SGP30 disabled as a result of an i2c error")

    def debug(self):
        if self.enabled:
            self.logger.debug("calibrating...")
            self.logger.info(f"eCO2: {self.sensor.eCO2} ppm")
            self.logger.info(f"TVOC: {self.sensor.TVOC} ppb")
        else:
            self.logger.error("sgp30 disabled as a result of an i2c error")

    def read(self) -> Dict:
        if not self.enabled:
            return []
        timestamp = time.time_ns()
        return [
                {
                    "measurement": "co2",
                    "tags": {
                        "location": self.location.to_string(),
                        "sensor": self.name,
                        "reading": "co2"
                        },
                    "time": timestamp,
                    "fields": {
                        "field": self.sensor.eCO2
                        }
                    },
                {
                    "measurement": "tvoc",
                    "tags": {
                        "location": self.location.to_string(),
                        "sensor": self.name,
                        "reading": "tvoc"
                        },
                    "time": timestamp,
                    "fields": {
                        "field": self.sensor.TVOC
                        }
                    } 
                ]

