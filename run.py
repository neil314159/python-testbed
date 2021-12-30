import gspread
import curses
from curses import wrapper

from google.oauth2.service_account import Credentials

stdscr = curses.initscr()

def main(stdscr):
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    
    stdscr.addstr("test")
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))
    #stdscr.refresh()
    #stdscr.getkey()

print('Welcome to Love Sandiwches automation')
wrapper(main)