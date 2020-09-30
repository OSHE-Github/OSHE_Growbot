import curses
from curses import wrapper
import sys

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
        main_screen.clear()
        print_keys(key, main_screen)
        
        if key == "q":
            sys.exit()
        
        print_line_bottom_center("Use the above keys to drive the robot.", main_screen)
        print_line_bottom_center("Press q to exit.", main_screen, 1)
        main_screen.refresh()

wrapper(main)
