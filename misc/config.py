import json
from misc.units import Temp
from misc.location import Location


class Config(object):

    def __init__(self, path: str):
        with open(path) as f:
            container = json.load(f)

        self.db = container['database']
        self.pressure = container['pressure']
        self.temperature = Temp.get_from_string(container['temperature'])
        self.location = Location.get_from_string(container['location'])
        self.debug = container['debug']
