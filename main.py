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


def main(args):
    with open(args.config) as c:
        config = json.load(c)
    db = DB(config['database'])
    
    temperature = Temp.get_from_string(config['temperature'])
    i2c = busio.I2C(board.SCL, board.SDA)
    
    sensors = [
            BME680(i2c, temperature, config['pressure'], config['location']), 
            SGP30(i2c, temperature, config['location'])
            ]
    logging.info("Done initializing sensors")

    while True:
        response = list()
        for sensor in sensors:
            sensor.calibrate(5)
            if config['debug']:
                sensor.debug()
            response.extend(sensor.read())
        if config['debug']:
            logging.warn(response)
        db.write(response)
        time.sleep(120)
    db.close()

if __name__ == "__main__":
    colorlog.basicConfig(level=logging.DEBUG,
            format='%(log_color)s%(levelname)s:\t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s')
    parser = argparse.ArgumentParser()
    default_path = os.path.expanduser('~/config.json')
    parser.add_argument('-c', '--config', help="Path to the config", default=default_path)
    args = parser.parse_args(sys.argv[1:])

    main(args)
