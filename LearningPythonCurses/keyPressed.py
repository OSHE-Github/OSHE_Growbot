import curses
from curses import wrapper

def main(main_screen):

    # Turn blinking cursor off.
    curses.curs_set(0)

    # Get the number of rows and columns so that text can be centered in the terminal window.
    num_rows, num_cols = main_screen.getmaxyx()

    # Prints a line in the center of the specified screen
    def print_center(message, screen):
        
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

    # Ask the user for input.
    print_center("Press any key...", main_screen)

    # Loop forever to show the keycode and character the user enters.
    while True:
        c = main_screen.getch()
        
        # Get the number of rows and columns so that text can be centered in the terminal window.
        num_rows, num_cols = main_screen.getmaxyx()
        
        main_screen.clear()
        
        # Convert the key to ASCII and print ordinal value
        print_center("You pressed %s which is keycode %d." % (chr(c), c), main_screen)

wrapper(main)

# Turn blinking cursor on.
curses.curs_set(1)
