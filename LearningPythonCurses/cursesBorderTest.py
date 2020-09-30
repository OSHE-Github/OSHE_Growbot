import curses
from curses import wrapper

def main(main_screen):

    # Turn blinking cursor off.
    curses.curs_set(0)

    # Get the number of rows and columns so that text can be centered in the terminal window.
    num_rows, num_cols = main_screen.getmaxyx()

    print("Rows:    %d" % num_rows)
    print("Columns: %d" % num_cols)


    # Prints a border on the specified window
    def print_border(window):
        
        # Get the number of rows and columns so that text can be centered in the terminal window.
        num_rows, num_cols = window.getmaxyx()
        
        horizontal_border = "─"*(num_cols-2)
        vertical_border = "│\n"*(num_rows-3)+"|"
        top_left_corner_border = "┌"
        top_right_corner_border = "┐"
        bottom_right_corner_border = "┘"
        bottom_left_corner_border = "└"
        
        # Draw the top row
        top_border = top_left_corner_border+horizontal_border+top_right_corner_border
        window.addstr(0, 0, top_border)
        
        # # Draw the right border
        # right_border = vertical_border
        # window.addstr(num_cols-1, 1, right_border)
        
        # # Draw the bottom row
        bottom_border = bottom_left_corner_border+horizontal_border+bottom_right_corner_border
        window.addstr(num_rows-2, 0, bottom_border)
        
        window.refresh()

    # lines, columns, start line, start column
    window_border = curses.newwin(num_rows-1, num_cols-1, 0, 0)
    
    while True:
    
        if main_screen.getch() == curses.KEY_RESIZE:
            curses.resizeterm(*main_screen.getmaxyx())
            main_screen.clear()
            main_screen.border()
            main_screen.refresh()
        
    
    #print_border(window_border)

    # curses.napms(3000)


wrapper(main)
