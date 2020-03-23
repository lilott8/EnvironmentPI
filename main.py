import colorlog
import logging

import board
import time
import busio
import adafruit_sgp30

def do_i2c():
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
    
    #logging.warn(f"SGP30 serial #: {[hex(i) for i in sgp30.serial]}")
    
    sgp30.iaq_init()
    sgp30.set_iaq_baseline(0x8973, 0x8AAE)

    logging.info(f"eCO2: {sgp30.eCO2}ppm \t TVOC: {sgp30.TVOC}")

def main():
    logging.info("Hello, world")
    do_i2c()

if __name__ == "__main__":
    colorlog.basicConfig(level=logging.DEBUG,
                         format='%(log_color)s%(levelname)s:\t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s')
    main()
