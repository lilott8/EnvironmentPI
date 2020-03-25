import colorlog
import logging
import board
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
    db = DB(args.database)
    temp = Temp.get_from_string(args.temp)
    i2c = busio.I2C(board.SCL, board.SDA)
    logging.info(f"Using: {temp} for temp")
    sensors = [BME680(i2c, temp, args.pressure, args.loc), SGP30(i2c, temp, args.loc)]

    x = 0
    while True:
        response = list()
        for sensor in sensors:
            sensor.calibrate(5)
            sensor.debug()
            response.extend(sensor.read())
            logging.warn(response)
        db.write(response)
        x += 1
        if x > 5:
            break
    db.close()

if __name__ == "__main__":
    colorlog.basicConfig(level=logging.DEBUG,
            format='%(log_color)s%(levelname)s:\t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s')
    parser = argparse.ArgumentParser()
    default_path = os.path.expanduser('~/config.json')
    parser.add_argument('-db', '--database', help="Path to the database config", default=default_path)
    parser.add_argument('-p', '--pressure', help='Standing pressure of your location', default=760.0, type=float)
    parser.add_argument('-t', '--temp', help="Units F|C|K", choices=['f', 'c', 'k'], default="f")
    parser.add_argument("-l", "--loc", help="Location of sensor", choices=["living_room", "master_bed", "kids_room_1", "kids_room_2", "kitchen"], default="living_room")
    
    args = parser.parse_args(sys.argv[1:])

    main(args)
