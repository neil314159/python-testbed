import gspread
import curses
from curses import wrapper

from google.oauth2.service_account import Credentials

stdscr = curses.initscr()

def main(stdscr):
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

print('Welcome to Love Sandiwches automation')
wrapper(main)