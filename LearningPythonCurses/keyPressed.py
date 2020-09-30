import curses
from curses import wrapper

def main(main_screen):

    # Turn blinking cursor off.
    curses.curs_set(0)

    # Get the number of rows and columns so that text can be centered in the terminal window.
    num_rows, num_cols = main_screen.getmaxyx()

    # Prints a line in the center of the specified screen
    def print_center(message, screen):
        
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
        screen.refresh()
        
    # Prints a border on the specified window
    def print_border(window):
        
        # Get the number of rows and columns so that text can be centered in the terminal window.
        num_rows, num_cols = window.getmaxyx()
        
        horizontal_border = "─"*(num_cols-2)
        vertical_border = "│"*(num_rows-2)
        top_left_corner_border = "┌"
        top_right_corner_border = "┐"
        bottom_right_corner_border = "┘"
        bottom_left_corner_border = "└"

        # Draw the top row
        top_border = top_left_corner_border+horizontal_border+top_right_corner_border
        window.addstr(0, 0, top_border)
        window.refresh()

    # Ask the user for input.
    print_center("Press any key...", main_screen)
    
    
    # lines, columns, start line, start column
    quit_dialog = curses.newwin(5, 30, 0, 0)
    
    # lines, columns, start line, start column
    window_border = curses.newwin(num_cols, num_rows, 0, 0)
    
    # lines, columns, start line, start column
    remote_control_main = curses.newwin(num_cols-2, num_rows-2, 1, 1)
    
    quit_dialog.addstr("┌────────────────────────┐\n")
    quit_dialog.addstr("│ Press `Ctrl+c` to quit │\n")
    quit_dialog.addstr("└────────────────────────┘\n")
    quit_dialog.refresh()

    # Loop forever to show the keycode and character the user enters.
    while True:
        c = remote_control_main.getch()
        
        # Get the number of rows and columns so that text can be centered in the terminal window.
        num_rows, num_cols = remote_control_main.getmaxyx()
        
        remote_control_main.clear()
        
        quit_dialog.clear()
        quit_dialog.addstr("┌────────────────────────┐\n")
        quit_dialog.addstr("│ Press `Ctrl+c` to quit │\n")
        quit_dialog.addstr("└────────────────────────┘\n")
        quit_dialog.refresh()
        
        # Convert the key to ASCII and print ordinal value
        print_center("You pressed %s which is keycode %d. " % (chr(c), c), remote_control_main)

wrapper(main)

# Turn blinking cursor on.
curses.curs_set(1)
