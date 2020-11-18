# Simple demo of continuous ADC conversion mode for channel 0 of the ADS1x15 ADC.
# Author: Tony DiCola
# License: Public Domain
import time
import odrive
from odrive.enums import *

# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 2/3 

my_drive = odrive.find_any()
my_drive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

while my_drive.axis1.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

my_drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

start = time.time()

while (time.time() - start) <= 30.0:   
    
    # Read the specified ADC channel using the previously set gain value.
    value = adc.read_adc(1, gain=GAIN)/500
        
    print('| {0:>6} |'.format(value))

    my_drive.axis1.controller.input_vel = value

