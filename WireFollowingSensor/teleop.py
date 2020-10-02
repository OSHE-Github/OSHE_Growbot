#!/usr/bin/env python3

from __future__ import print_function

import odrive
from odrive.enums import *
import time
import math
import curses
from curses import wrapper
import sys


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

# Save the config
#my_drive.save_configuration()

###################### CURSES PART ##########################
# Prints a line in the center of the specified screen
def print_line_center(message, screen):
    
    # Get the number of rows and columns so that text can be centered in the terminal window.
    num_rows, num_cols = screen.getmaxyx()
    
    # Calculate center row
    middle_row = int(num_rows / 2)
    
    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message
    
    # Draw the text
    screen.addstr(middle_row, x_position, message)

# Prints a line in the center of the specified screen on the bottom
def print_line_bottom_center(message, screen, offset=0):
    
    # Get the number of rows and columns so that text can be centered in the terminal window.
    num_rows, num_cols = screen.getmaxyx()
    
    # Calculate center row
    middle_row = int(num_rows / 2 + num_rows / 4 + offset)
    
    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message
    
    # Draw the text
    screen.addstr(middle_row, x_position, message)

# Prints the driving keys at the center of the specified screen
def print_keys(key, screen):
    
    # Get the number of rows and columns so that text can be centered in the terminal window.
    num_rows, num_cols = screen.getmaxyx()
    
    keys = "j k l ;"
    
    if key == "j":
        
        arrows = "<       "
        
    elif key == "k":
        
        arrows = "  ^     "
        
    elif key == "l":
        
        arrows = "    v   "
        
    elif key == ";":
        
        arrows = "      >"
        
    else:
        
        arrows = "< ^ v >"
    
    # Calculate center row
    middle_row = int(num_rows / 2)
    
    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(keys) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message
    
    # Draw the text
    screen.addstr(middle_row+1, x_position, arrows)
    screen.addstr(middle_row, x_position, keys)

# Checks and resizes the window if the terminal has changed size
def check_screen_resize(screen):
    
    if screen.getch() == curses.KEY_RESIZE:
        curses.resizeterm(*screen.getmaxyx())
        screen.clear()
        screen.border()
        screen.refresh()

    
def main(main_screen):
    
    # odrive stuffs
    t0 = time.monotonic()
    setpoint = 0
    
    # Turns off the cursor
    curses.curs_set(0)
    
    # Initialize the screen the first time.before the loop starts
    key = "b"
    main_screen.border()
    print_keys(key, main_screen)
    print_line_bottom_center("Use the above keys to drive the robot.", main_screen)
    print_line_bottom_center("Press q to exit.", main_screen, 1)
    main_screen.refresh()
    
    while True:
        
        # check_screen_resize(main_screen)
        main_screen.border()
        key = chr(main_screen.getch())
       
        if key == "q":
            sys.exit()
        elif key == "j":
            setpoint = setpoint + 100
            my_drive.axis0.controller.pos_setpoint = setpoint
            my_drive.axis1.controller.pos_setpoint = setpoint
        elif key == "k":
            setpoint = setpoint + 100
            my_drive.axis0.controller.pos_setpoint = setpoint
            my_drive.axis1.controller.pos_setpoint = -setpoint
        elif key == "l":
            setpoint = setpoint + 100
            my_drive.axis0.controller.pos_setpoint = -setpoint
            my_drive.axis1.controller.pos_setpoint = setpoint
        elif key == ";":
            setpoint = setpoint + 100
            my_drive.axis0.controller.pos_setpoint = -setpoint
            my_drive.axis1.controller.pos_setpoint = -setpoint

        main_screen.clear()
        print_keys(key, main_screen)
        
        
        #time.sleep(0.01)
        
        
        
        print_line_bottom_center("Use the above keys to drive the robot.", main_screen)
        print_line_bottom_center("Press q to exit.", main_screen, 1)
        main_screen.refresh()

wrapper(main)


