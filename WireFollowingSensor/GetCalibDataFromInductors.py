# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1 # 2/3 
    
while (True):
    
    # Read the specified ADC channel using the previously set gain value.
    value1 = abs(adc.read_adc(1, gain=GAIN)) + 1
    value0 = abs(adc.read_adc(0, gain=GAIN)) + 1
    if (value0 < 1000):
        value0 = 4.1902*pow(value0, -0.105)
    elif (1000 < value0 < 7300):
        value0 = (pow(10, -8)*pow(value0, 2)) - (0.0003*value0) + 2.2921
    elif (7300 < value0):
        value0 = (-6*pow(10, -12)*pow(value0, 3)) + (2*pow(10, -7)*pow(value0, 2)) - (0.0014*value0) + 5.2372
    bar0 = "█"*int(value0*2)
    bar1 = 1#"█"*int(value1*2)
    print('| {0:>6} | {2:>10} | {3:>10} | {1:>6} |'.format(value1, value0, bar1, bar0))
