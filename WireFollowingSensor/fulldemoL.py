from __future__ import print_function

import odrive
from odrive.enums import *
import time
import math
import time
import Adafruit_ADS1x15

# motor code
print("finding an odrive...")
my_drive = odrive.find_any()
Calibrate motor and wait for it to finish
print("starting calibration...")
my_drive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while my_drive.axis1.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)
my_drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
print("Bus voltage is " + str(my_drive.vbus_voltage) + "V")
my_drive.axis1.controller.pos_setpoint = 3.14
print("Position setpoint is " + str(my_drive.axis0.controller.pos_setpoint))
for i in [1,2,3,4]:
    print('voltage on GPIO{} is {} Volt'.format(i, my_drive.get_adc_voltage(i)))

# sensor code
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
adc.start_adc(1, gain=GAIN)
start = time.time()

while True:
	# continuously read sensor input
    value = adc.get_last_result()
    print('Channel 1: {0}'.format(value))
    time.sleep(0.5)

    # continuously move motor
    if (value == max * 0.8):     	# very close to wire
	  setpoint = setpoint
	else if (value == max * 0.6):   # close to wire
	  setpoint = setpoint + 0.5
	else: 							# far from wire
	  setpoint = setpoint + 1

    print("goto " + str(int(setpoint)))
    my_drive.axis1.controller.pos_setpoint = setpoint
    time.sleep(0.01)
