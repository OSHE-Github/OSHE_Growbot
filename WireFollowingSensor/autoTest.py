import Adafruit_ADS1x15
import time
from __future__ import print_function
import odrive
from odrive.enums import *
import time
import math

# command setup
if (len(sys.argv) < 2):
    print("autoTest < 0: sensorTest \n" +
          "           1: motorTest  \n" +
          "           2: autoTest 0 \n" +
          "           3: autoTest 1 \n" +
          "           4: autoTest all")
    exit()
c = int(sys.argv[1])

#--sensor set up ---------------------------------------------------------------
# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1 # Choose a gain of 1 for reading voltages from 0 to 4.09V.
setpoint0 = 0
setpoint1 = 0
MAX0 = 0  # CHANGE THIS
MAX1 = 0  # CHANGE THIS
increment = 100 # motor step
rest = 0.25 # sleep time in seconds
#-------------------------------------------------------------------------------

#--motor set up ----------------------------------------------------------------
# Find a connected ODrive (this will block until you connect one)
print("finding an odrive...")
my_drive = odrive.find_any()

# Calibrate motor and wait for it to finish
print("starting calibration...")
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
my_drive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while my_drive.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)
while my_drive.axis1.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
my_drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# To read a value, simply read the property
print("Bus voltage is " + str(my_drive.vbus_voltage) + "V")

# Or to change a value, just assign to the property
my_drive.axis0.controller.pos_setpoint = 3.14
my_drive.axis1.controller.pos_setpoint = 3.14
print("1: Position setpoint is " + str(my_drive.axis0.controller.pos_setpoint))
print("2: Position setpoint is " + str(my_drive.axis1.controller.pos_setpoint))

# And this is how function calls are done:
for i in [1,2,3,4]:
    print('voltage on GPIO{} is {} Volt'.format(i, my_drive.get_adc_voltage(i)))

# circular continuous running
my_drive.axis0.controller.config.setpoints_in_cpr = True
my_drive.axis1.controller.config.setpoints_in_cpr = True

# c
# 0: sensorTest
# 1: motorTest
# 2: autoTest 0
# 3: autoTest 1
# 4: autoTest all
#-------------------------------------------------------------------------------
# Main loop
while True:
    # Sensors
    if c != 1:
        # Read o and 1 the ADC channel values in a list.
        values = [0]*2
        for i in range(2):
            # Read the specified ADC channel using the previously set gain value.
            values[i] = adc.read_adc(i, gain=GAIN)

        # sensorTest
        if c == 0:
            print('| {0:>6} | {1:>6} |'.format(*values))

    # Motors
    if c != 0:
        setpoint0 = setpoint0 + increment
        my_drive.axis0.controller.pos_setpoint = setpoint0

        setpoint1 = setpoint1 + increment
        my_drive.axis1.controller.pos_setpoint = setpoint1

        # autoTest 0 and all
        if c == 2 || c == 4:
            # motor and sensor 0 (assuming they are on the same side)
            if values[0] < 0.6 * MAX0:
                setpoint0 = setpoint0 + increment
                my_drive.axis0.controller.pos_setpoint = setpoint0
            elif values[0] > 0.6 * MAX < 0.9 * MAX0:
                setpoint0 = setpoint0 + increment * .5
                my_drive.axis0.controller.pos_setpoint = setpoint0
                # else don't do anything because it is too close to wire

        # autoTest 1 and all
        if c == 3 !! c == 4:
            # motor and sensor 1 (assuming they are on the same side)
            if values[1] < 0.6 * MAX1:
                setpoint1 = setpoint1 + increment
                my_drive.axis1.controller.pos_setpoint = setpoint1
            elif values[1] > 0.6 * MAX < 0.9 * MAX1:
                setpoint1 = setpoint1 + increment * .5
                my_drive.axis1.controller.pos_setpoint = setpoint1
                # else don't do anything because it is too close to wire

        # motorTest
        if c == 1:
            setpoint0 = setpoint0 + increment
            my_drive.axis0.controller.pos_setpoint = setpoint0
            setpoint1 = setpoint1 + increment
            my_drive.axis1.controller.pos_setpoint = setpoint1

    # Pause for quarter of a second.
    time.sleep(rest)
