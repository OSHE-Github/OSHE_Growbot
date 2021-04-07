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

# To read a value, simply read the property

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


def WireFollowingLoop():
    # Default speed in turns per second.
    drivingSpeed = 1.5

    # Start Robot Driving straight.
    my_drive.axis0.controller.input_vel = drivingSpeed
    my_drive.axis1.controller.input_vel = -drivingSpeed

    timeOfWireSense = time.time() 
    timeSince = 0
    while (True):
    
        # Read the specified ADC channel using the previously set gain value.
        value1 = abs(adc.read_adc(1, gain=GAIN)) + 1
        value0 = abs(adc.read_adc(0, gain=GAIN)) + 1
        bar1 = "█"*int(value1/2400)
        bar0 = "█"*int(value0/2400)
        print('| {0:>6} | {2:>10} | {3:>10} | {1:>6} |'.format(value1, value0, bar1, bar0))

        # Check to make sure that robot is driving straight.
        if (abs(value0 - value1) < 100):
            my_drive.axis0.controller.input_vel = drivingSpeed
            my_drive.axis1.controller.input_vel = -drivingSpeed
            timeSince = time.time() - timeOfWireSense
        # If not, then correct by value of encoders.
        elif (value0 > value1):
            my_drive.axis0.controller.input_vel = (drivingSpeed*1.75) + drivingSpeed*(value0/14000)
            my_drive.axis1.controller.input_vel = -(drivingSpeed/3)
            timeOfWireSense = time.time()
        elif (value1 > value0):
            my_drive.axis0.controller.input_vel = drivingSpeed/3
            my_drive.axis1.controller.input_vel = -((drivingSpeed*1.75) + drivingSpeed*(value1/14000))
            timeOfWireSense = time.time()

        if (timeSince > 3):
            my_drive.axis0.controller.input_vel = 0
            my_drive.axis1.controller.input_vel = 0
            print("The robot has lost the wire!")
            break

    # To read a value, simply read the property
    print("Bus voltage is {0:>5}V".format(my_drive.vbus_voltage))
    return

while (True):
    # Wait for user input to start driving loop.
    char = input("Enter \"y\" to restart driving loop, or \"n\" to quit: ")
    
    if (char == "y"):
        WireFollowingLoop()
    else:
        my_drive.axis0.requested_state = AXIS_STATE_IDLE
        my_drive.axis1.requested_state = AXIS_STATE_IDLE
        break
