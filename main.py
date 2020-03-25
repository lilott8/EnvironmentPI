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


def bme_sensor():
    i2c = busio.I2C(board.SCL, board.SDA)
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

    bme680.sea_level_pressure = 1013.25
    logging.info(f"Temperature: {bme680.temperature}")
    logging.info(f"Gas: {bme680.gas}")
    logging.info(f"Humidity: {bme680.humidity}")
    logging.info(f"Pressure: {bme680.pressure}")
    logging.info(f"Altitude: {bme680.altitude}")

def sgp_sensor():
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

    sgp30.iaq_init()
    sgp30.set_iaq_baseline(0x8973, 0x8AAE)

    logging.info(f"eCO2: {sgp30.eCO2}ppm \t TVOC: {sgp30.TVOC}")

def main(args):
    # db = DB(args.database)
    temp = Temp.get_from_string(args.temp)
    i2c = busio.I2C(board.SCL, board.SDA)
    logging.info(f"Using: {temp} for temp")
    sensors = [BME680(i2c, temp, args.pressure), SGP30(i2c, temp)]

    #sgp_sensor()
    #bme_sensor()

    x = 0
    while True:
        for sensor in sensors:
            sensor.calibrate()

        for sensor in sensors:
            response = sensor.read()
            #db.write(response)
        x += 1
        if x > 5:
            break

    logging.info("Hello, world")
    sgp_sensor()

if __name__ == "__main__":
    colorlog.basicConfig(level=logging.DEBUG,
            format='%(log_color)s%(levelname)s:\t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s')
    parser = argparse.ArgumentParser()
    default_path = os.path.expanduser('~/config.json')
    parser.add_argument('-db', '--database', help="Path to the database config", default=default_path)
    parser.add_argument('-p', '--pressure', help='Standing pressure of your location', default=760.0, type=float)
    parser.add_argument('-t', '--temp', help="Units F|C|K", choices=['f', 'c', 'k'], default="f")
    
    args = parser.parse_args(sys.argv[1:])

    main(args)
