import time

from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

i=0

while i < 5:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()
    # read temperature from the temperature sensor
    temp = ss.get_temp()
    print("outside moisture: " + str(touch))
    time.sleep(5)

    touch = ss.moisture_read()
    temp = ss.get_temp()
    print("material moisture: " + str(touch))
    time.sleep(5)


    i = i + 1
