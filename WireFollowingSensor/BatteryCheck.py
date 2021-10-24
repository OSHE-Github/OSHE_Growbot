# Import the ADS1x15 module.
import Adafruit_ADS1x15
import os

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 2/3 

# Read the voltage divider ADC
value = adc.read_adc(3, gain=GAIN)
#print(value)
# I believe that the ADC at GAIN = 2/3 can yield: voltage = 0.001883645 * value
voltage = value*0.001883645
#print("{0}V".format(voltage))
if (voltage < 22.4):
    os.system("shutdown now")
