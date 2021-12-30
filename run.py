import curses
import time
 
# get_io is using random values, but a real I/O handler would be here
def get_io():
    import random
    global value1, value2
    value1 = random.randint(1,30)
    value2 = random.randint(1,30)
 
bar = '█' # an extended ASCII 'fill' character
stdscr = curses.initscr()
height, width = stdscr.getmaxyx() # get the window size
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
 
# layout the header and footer
stdscr.addstr(1,1, " " * (width -2),curses.color_pair(1) )
stdscr.addstr(1,15, "Raspberry Pi I/O",curses.color_pair(1) )
stdscr.hline(2,1,"_",width)
stdscr.addstr(height -1,1, " " * (width -2),curses.color_pair(1) )
stdscr.addstr(height -1,5, "Hit q to quit",curses.color_pair(1) )
 
# add some labels
stdscr.addstr(4,1, "Pi Sensor 1 :")
stdscr.addstr(8,1, "Pi Sensor 2 :")
 
# Define windows to be used for bar charts
win1 = curses.newwin(3, 32, 3, 15) # curses.newwin(height, width, begin_y, begin_x)
win2 = curses.newwin(3, 32, 7, 15) # curses.newwin(height, width, begin_y, begin_x)
 
# Use the 'q' key to quit
k = 0
while (k != ord('q')):
    get_io() # get the data values
    win1.clear()
    win1.border(0)
    win2.clear()
    win2.border(0)
# create bars bases on the returned values
    win1.addstr(1, 1, bar * value1, curses.color_pair(2))
    win1.refresh()
    win2.addstr(1, 1, bar * value2 , curses.color_pair(3))
    win2.refresh()
# add numeric values beside the bars
    stdscr.addstr(4,50, str(value1) + " Deg ",curses.A_BOLD )
    stdscr.addstr(8,50, str(value2) + " Deg ",curses.A_BOLD )
    stdscr.refresh()
    time.sleep(2)
    stdscr.nodelay(1)
    k = stdscr.getch() # look for a keyboard input, but don't wait
 
curses.endwin() # restore the terminal settings back to the original