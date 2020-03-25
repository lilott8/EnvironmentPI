from enum import IntEnum


class Temp(IntEnum):
    CELSIUS = 1
    FAHRENHEIT = 2
    KELVIN = 3

    def normalize(self, quantity: float) -> float:
        if self == Temp.CELSIUS:
            return quantity
        elif self == Temp.FAHRENHEIT:
            return (quantity * (9/5.0)) + 32
        elif self == Temp.KELVIN:
            return quantity - 273.15
        else:
            return quantity
    
    def __str__(self):
        if self == Temp.CELSIUS:
            return "C"
        elif self == Temp.FAHRENHEIT:
            return "F"
        elif self == Temp.KELVIN:
            return "K"
        else:
            return "C"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def get_from_string(temp: str):
        if temp.lower() == "f":
            return Temp.FAHRENHEIT
        elif temp.lower() == "k":
            return Temp.KELVIN
        else:
            return Temp.CELSIUS
