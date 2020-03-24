from .base_sensor import BaseSensor


class SGP30(BaseSensor):

    def __init__(self):
        super().__init__()

    def calibrate(self):
        pass

    def read(self):
        pass
