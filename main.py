import signal
import colorlog
import logging
import board
import json
import time
import busio
import adafruit_sgp30
import adafruit_bme680
import argparse
import sys
from sensors.bme680 import BME680
from sensors.sgp30 import SGP30
from misc.db import DB
from misc.units import Temp
import os
from typing import Dict


class Environment(object):

    def __init__(self, config: str):
        self.logger = colorlog.getLogger(self.__class__.__name__)
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
        with open(args.config) as c:
            self.config = json.load(c)
        self.db = DB(self.config['database'])
        self.temperature = Temp.get_from_string(self.config['temperature'])

        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensors = [
                BME680(i2c, self.temperature, self.config['pressure'], self.config['location']), 
                SGP30(i2c, self.temperature, self.config['location'])
                ]
        self.alive = True
        pass

    def run(self):
        for sensor in self.sensors:
            sensor.calibrate(2)
        logging.info("Done initializing sensors")

        while self.alive:
            response = list()
            for sensor in self.sensors:
                sensor.calibrate(5)
                if self.config['debug']:
                    sensor.debug()
                response.extend(sensor.read())
            if self.config['debug']:
                self.logger.warn(response)
            self.db.write(response)
            time.sleep(120)
        self.db.close()

    def shutdown(self, signum, frame):
        self.logger.warn("Shutting down environment")
        self.alive = False

if __name__ == "__main__":
    colorlog.basicConfig(level=logging.DEBUG,
            format='%(log_color)s%(levelname)s:\t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s')
    parser = argparse.ArgumentParser()
    default_path = os.path.expanduser('~/config.json')
    parser.add_argument('-c', '--config', help="Path to the config", default=default_path)
    args = parser.parse_args(sys.argv[1:])

    environment = Environment(args)
    environment.run()
