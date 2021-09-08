#Zach Arnold
#Open Source Hardware Enterprise
#Growbot
#Created: 2/25/2020
#Last Modified: 4/2/2020
#Description: This python file consists of functions used for the Soil Sensor

import time
import board
import busio
import digitalio
from adafruit_seesaw.seesaw import Seesaw

A1 = digitalio.DigitalInOut(board.D22)
A1.direction = digitalio.Direction.OUTPUT
A2 = digitalio.DigitalInOut(board.D23)
A2.direction = digitalio.Direction.OUTPUT
sleep = digitalio.DigitalInOut(board.D18)
sleep.direction = digitalio.Direction.OUTPUT
B2 = digitalio.DigitalInOut(board.D27)
B2.direction = digitalio.Direction.OUTPUT
B1 = digitalio.DigitalInOut(board.D17)
B1.direction = digitalio.Direction.OUTPUT




#home sensor setup
#homeSensorPin = 30
#GPIO.setup(homeSensorPin, GPIO.IN)

#Soil sensor connection and setup
soilAdr = 0x36
i2c_bus = busio.I2C(board.SCL, board.SDA)
ss = Seesaw(i2c_bus, soilAdr)

#number of steps to move sensor down from home
sensorSteps = 100

def read_soil():
    #all of the sensor reading stuff from adafruit
    time.sleep(1)
    touch = ss.moisture_read()
    temp = ss.get_temp()
    time.sleep(1)
    return touch, temp

#def sensor_home():
    #motor up until home switch
    #homeSensorState = GPIO.input(homeSensorPin)
    #while (homeSensorState is True):
        #homeSensorState = GPIO.input(homeSensorPin)

    #print("Homing sensor...\n")

def step( stepVal ):
    if stepVal == 0:
        A1.value = True
        A2.value = False
        B1.value = True
        B2.value = False
    elif stepVal == 1:
        A1.value = False
        A2.value = True
        B1.value = True
        B2.value = False
    elif stepVal == 2:
        A1.value = False
        A2.value = True
        B1.value = False
        B2.value = True
    elif stepVal == 3:
        A1.value = True
        A2.value = False
        B1.value = False
        B2.value = True

def sensor_down():
    #move motor down X (value determined from testing) to go into soil, then read_soil
    #sensor_home()

    # enable driver
    sleep.value = True

    print("Deploying the sensor...\n")

    # start stepping
    for s in range(sensorSteps):
        i = s % 4
        # step motor
        step(i)
        time.sleep(0.01)




sensor_down()
#while True:

    #print(read_soil())
    #time.sleep(5)
