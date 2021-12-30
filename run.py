import curses

screen = curses.initscr()

try:
    screen.border(0)
    box1 = screen.subwin(20, 20, 5, 5)
    box1.box()
    screen.getch()

finally:
    curses.endwin()