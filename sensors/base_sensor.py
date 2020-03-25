import abc
import colorlog
from typing import Dict


class BaseSensor(metaclass=abc.ABCMeta):

    def __init__(self, name: str, temp, loc: str):
        self.logger = colorlog.getLogger(name)
        self.name = name
        self.temp = temp
        self.location = loc

    @abc.abstractmethod
    def debug(self):
        pass

    @abc.abstractmethod
    def calibrate(self, iterations: int):
        pass

    @abc.abstractmethod
    def read(self) -> Dict:
        pass

