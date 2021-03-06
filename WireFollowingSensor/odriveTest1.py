#!/usr/bin/python3
"""
Testing out how to get remote controll working on the robot.
"""

from __future__ import print_function

import odrive
from odrive.enums import *
import time

# Find a connected ODrive (this will block until you connect one)
print("finding an odrive...")
my_drive = odrive.find_any()

# Calibrate motors and wait for it to finish
print("starting calibration...")
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while my_drive.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)
#my_drive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
#while my_drive.axis1.current_state != AXIS_STATE_IDLE:
    #time.sleep(0.1)
print("sanity test")
my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
#my_drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

my_drive.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
my_drive.axis0.controller.input_vel = 1.0
time.sleep(10)
my_drive.axis0.controller.input_vel = 5.0
time.sleep(10)
my_drive.axis0.controller.input_vel = 1.0
time.sleep(10)
my_drive.axis0.controller.input_vel = 0.0 
