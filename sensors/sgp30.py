from .base_sensor import BaseSensor
from typing import Dict
from misc.units import Temp
import adafruit_sgp30
from busio import I2C


class SGP30(BaseSensor):

    def __init__(self, i2c: I2C, temp: Temp):
        super().__init__(self.__class__.__name__, temp)
        self.sensor = adafruit_sgp30.Adafruit_SGP30(i2c)
        self.sensor.iaq_init()
        self.sensor.set_iaq_baseline(0x8973, 0x8AAE)

    def calibrate(self):
        self.logger.debug("calibrating...")
        self.logger.info(f"eCO2: {self.sensor.eCO2} ppm")
        self.logger.info(f"TVOC: {self.sensor.TVOC} ppb")

    def read(self) -> Dict:
        return {}

