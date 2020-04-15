#!/usr/bin/env python3
"""
Example usage of the ODrive python library to monitor and control ODrive devices
"""

from __future__ import print_function

import odrive
from odrive.enums import *
import time
import math

# Set Up
print("finding an odrive...")
my_drive = odrive.find_any("serial:/dev/ttyS0")
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while my_drive.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)
my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
##

# quick test
my_drive.axis0.controller.pos_setpoint = 10000

## circle
my_drive.axis0.controller.config.setpoints_in_cpr = True
##
