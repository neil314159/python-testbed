import gspread
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

from google.oauth2.service_account import Credentials

stdscr = curses.initscr()

def main(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    editwin = curses.newwin(5,30, 2,1)
    rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()
print('Welcome to Love Sandiwches2 automation')
wrapper(main)