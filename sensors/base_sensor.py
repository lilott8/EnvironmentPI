import abc
import colorlog
from typing import Dict
from misc.config import Config

class BaseSensor(metaclass=abc.ABCMeta):

    def __init__(self, name: str, config: Config):
        self.logger = colorlog.getLogger(name)
        self.config = config
        self.name = name
        self.temp = self.config.temperature
        self.location = self.config.location

    @abc.abstractmethod
    def debug(self):
        pass

    @abc.abstractmethod
    def calibrate(self, iterations: int):
        pass

    @abc.abstractmethod
    def read(self) -> Dict:
        pass

