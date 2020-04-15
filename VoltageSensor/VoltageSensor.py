#Zach Arnold
#Open Source Hardware Enterprise
#Growbot
#Created: 2/25/2020
#Last Modified: 4/2/2020
#Description: This python file consists of functions used for the Soil Sensor

# import the raspberry pi pin libraries and
import board
import time
import Adafruit_ADS1x15 as ADS

# Create an ADS1115 ADC (16-bit) instance.
ads = ADS.ADS1115()
GAIN = 1
#GAIN = 1


while True:
    #get sensor value
    sensorValue = adc.read_adc(4, gain=GAIN)
    #print("Sensor Val: " + str(sensorValue))
    #Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 50V):
    voltage = sensorValue * (4.096 / 32768.0) * 10.1

    print("Voltage ADC: " + str(sensorValue))
    print("Voltage: " + str(voltage))
    time.sleep(1)
