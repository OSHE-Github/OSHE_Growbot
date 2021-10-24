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
GAIN = 1 # 2/3 

my_drive = odrive.find_any()
my_drive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

while my_drive.axis1.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)
while my_drive.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

my_drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

#start = time.time()

while (1==1):   
    
    # Read the specified ADC channel using the previously set gain value.
    value1 = adc.read_adc(1, gain=GAIN)/4000
    value0 = adc.read_adc(0, gain=GAIN)/4000
     
    print('| {0:>8} | {0:>8} |'.format(value1*4000, value0*4000))

    my_drive.axis1.controller.input_vel = -value1
    my_drive.axis0.controller.input_vel = value0

