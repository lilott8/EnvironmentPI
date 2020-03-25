import abc
import colorlog
from typing import Dict


class BaseSensor(metaclass=abc.ABCMeta):

    def __init__(self, name: str, temp):
        self.logger = colorlog.getLogger(name)
        self.temp = temp

    @abc.abstractmethod
    def calibrate(self):
        pass

    @abc.abstractmethod
    def read(self) -> Dict:
        pass

