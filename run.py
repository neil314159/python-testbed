import curses

win = curses.initscr()

def main():

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)


    win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    win.addstr(1,1, "This is not blue")
    win.getch()
    win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)
    win.addstr(1,1, "This is now blue")
    win.getch()

main()