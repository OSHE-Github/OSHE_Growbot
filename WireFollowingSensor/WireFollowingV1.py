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

my_drive.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL # Or just 2.
my_drive.axis0.controller.config.input_mode = INPUT_MODE_VEL_RAMP
my_drive.axis0.controller.config.vel_ramp_rate = 50
my_drive.axis1.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL # Or just 2.
my_drive.axis1.controller.config.input_mode = INPUT_MODE_VEL_RAMP
my_drive.axis1.controller.config.vel_ramp_rate = 50

# Default speed in turns per second.
drivingSpeed = 1

# Start Robot Driving straight.
my_drive.axis0.controller.input_vel = drivingSpeed
my_drive.axis1.controller.input_vel = -drivingSpeed

while (1==1):   
    
    # Read the specified ADC channel using the previously set gain value.
    value1 = adc.read_adc(1, gain=GAIN)
    value0 = adc.read_adc(0, gain=GAIN)
     
    print('| {0:>8} | {1:>8} |'.format(value1, value0))

    # Check to make sure that robot is driving straight.
    if (value0 < 1000 and value1 < 1000):
       my_drive.axis0.controller.input_vel = drivingSpeed
       my_drive.axis1.controller.input_vel = -drivingSpeed 
    # If not, then correct by value of encoders.
    elif (value0 > 1000):
        my_drive.axis0.controller.input_vel = drivingSpeed + 4 + value0/14000
        my_drive.axis1.controller.input_vel = -(drivingSpeed/2)
    elif (value1 > 1000):
        my_drive.axis0.controller.input_vel = drivingSpeed/2
        my_drive.axis1.controller.input_vel = -(drivingSpeed + 4 + value1/14000)
