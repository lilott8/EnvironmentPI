import abc
import colorlog


class BaseSensor(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def calibrate(self):
        pass

    @abc.abstractmethod
    def read(self):
        pass

