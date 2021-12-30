import curses
import random
import time

g_map = (
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)

g_tileCharsMap = {0:' ', 1:'H'}

def drawMap(_screen, _map):
    for row in range(len(_map)):
        for col in range(len(_map[row])):
            _screen.addch(row, col, g_tileCharsMap[_map[row][col]])

stdscr = curses.initscr()
stdscr.nodelay(1) #cursor.getch won't wait for input
curses.curs_set(0) #hide cursor

drawMap(stdscr, g_map)

while(True):
    newX = random.randint(1, 8)
    newY = random.randint(1, 8)
    stdscr.addch(newX, newY, 'x')
    stdscr.refresh()
    time.sleep(0.1)
    stdscr.addch(newX, newY, ' ')

    if(stdscr.getch() >= 0): break #exit on any key pressed

curses.endwin()