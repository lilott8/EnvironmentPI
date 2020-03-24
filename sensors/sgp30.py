from .base_sensor import BaseSensor
from typing import Dict


class SGP30(BaseSensor):

    def __init__(self, ):
        super().__init__(self.__class__.__name__)

    def calibrate(self):
        self.logger.debug("calibrating...")

    def read(self) -> Dict:
        return {}

