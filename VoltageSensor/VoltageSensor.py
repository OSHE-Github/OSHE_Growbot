#Zach Arnold
#Open Source Hardware Enterprise
#Growbot
#Created: 2/25/2020
#Last Modified: 4/2/2020
#Description: This python file consists of functions used for the Soil Sensor

# import the raspberry pi pin libraries and
import board
import busio
import time
import Adafruit_ADS1x15

# setup I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
# Create an ADS1115 ADC (16-bit) instance.
ads = Adafruit_ADS1x15.ADS1115()
GAIN = 1
ads.start_adc(2, gain=GAIN)

while True:
    #get sensor value
    sensorValue = ads.get_last_result()
    print("Sensor Val: " + str(sensorValue))
    #Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 50V):
    voltage0 = sensorValue * (4.096 / 65536.0)
    voltage = voltage0 / (100000/(910000+100000))

    print("Voltage ADC: " + str(voltage0))
    print("Voltage: " + str(voltage))
    time.sleep(1)
