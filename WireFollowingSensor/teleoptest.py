#!/usr/bin/env python3

from __future__ import print_function

import time
import math
import curses
from curses import wrapper
import sys


# Find a connected ODrive (this will block until you connect one)
print("finding an odrive...")

# Calibrate motor and wait for it to finish
# To read a value, simply read the property

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

# Prints a line in the center of the specified screen at the top.
def print_line_top_center(message, screen, offset=0):
    
    # Get the number of rows and columns so that text can be centered in the terminal window.
    num_rows, num_cols = screen.getmaxyx()
    
    # Calculate center row
    middle_row = int(num_rows / 2 - num_rows / 4 - offset)
    
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
    
    # Turns off the cursor
    curses.curs_set(0)
    
    # Speed of the robot
    setpoint = 1

    # Initialize the screen the first time.before the loop starts
    key = "b"
    main_screen.border()
    print_keys(key, main_screen)
    print_line_top_center("{0} Turns/sec".format(setpoint), main_screen)
    print_line_bottom_center("Use the above keys to drive the robot (like vim).", main_screen)
    print_line_bottom_center("Press \"Space\" to stop robot, and \"q\" to exit this utility,", main_screen, 1)
    print_line_bottom_center("press \"f\" to go faster, and \"s\" to go slower.", main_screen, 2)
    main_screen.refresh()
    
    
    
    while True:
        
        # check_screen_resize(main_screen)
        main_screen.border()
        key = chr(main_screen.getch())
       
        if key == "q":
            sys.exit()
        elif key == "j":
            setpoint0 = setpoint
            setpoint1 = -setpoint/2
        elif key == "k":
            setpoint0 = setpoint
            setpoint1 = -setpoint
        elif key == "l":
            setpoint0 = -setpoint
            setpoint1 = setpoint
        elif key == ";":
            setpoint0 = setpoint/2
            setpoint1 = -setpoint
        elif key == "f":
            setpoint += 0.25
        elif key == "s":
            setpoint -= 0.25
        else:
            setpoint0 = 0
            setpoint1 = 0        
        
        main_screen.clear()
        print_keys(key, main_screen)
        print_line_top_center("{0} Turns/sec".format(setpoint), main_screen)
        print_line_bottom_center("Use the above keys to drive the robot (like vim).", main_screen)
        print_line_bottom_center("Press \"Space\" to stop robot, and \"q\" to exit this utility,", main_screen, 1)
        print_line_bottom_center("press \"f\" to go faster, and \"s\" to go slower.", main_screen, 2)
        time.sleep(0.01)
        main_screen.refresh()

wrapper(main)


