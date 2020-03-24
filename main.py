import colorlog
import logging
import board
import time
import busio
import adafruit_sgp30
import argparse
import sys
from sensors.bme680 import BME680
from sensors.sgp30 import SGP30


def sgp_sensor():
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

    sgp30.iaq_init()
    sgp30.set_iaq_baseline(0x8973, 0x8AAE)

    logging.info(f"eCO2: {sgp30.eCO2}ppm \t TVOC: {sgp30.TVOC}")

def main():
    sensors = [BME680(), SGP30()]


    logging.info("Hello, world")
    sgp_sensor()

if __name__ == "__main__":
    colorlog.basicConfig(level=logging.DEBUG,
            format='%(log_color)s%(levelname)s:\t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s')
    parser = argparse.ArgumentParser()
    parser.add_argument('-db', '--database', help="Path to the database config", required=True)
    
    parser.parse_args(sys.argv[1:])

    main()
