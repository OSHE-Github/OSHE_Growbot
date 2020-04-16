import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

while True:
    values = [0]*4
    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN)

    print('sensor 1: ' + values[0] + 'sensor 2: ' + values[1])

    time.sleep(0.5)
