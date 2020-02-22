import time

from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw

soilAdr = 0x36

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, soilAdr)

def read_soil:
    #all of the sensor reading stuff from adafruit
    time.sleep(1)
    touch = ss.moisture_read()
    temp = ss.get_temp()
    time.sleep(1)
    return touch, temp

def sensor_home:
    #motor up until home switch
    print("Homing sensor...\n")
def sensor_down:
    #move motor down X (value determined from testing) to go into soil, then read_soil
    print("Deploying the sensor...\n")
