import curses
from curses import A_REVERSE, window


def draw_menu(stdscr: window, items):
    for i, item in enumerate(items):
        stdscr.addstr('\n{} - {}'.format(i + 1, item))


def draw_toolbar(stdscr: window, text):
    empty = curses.COLS - len(text)
    fill = (' ' * empty)
    newtext = text + fill  # Fill with spaces
    stdscr.addstr(newtext, A_REVERSE)
    stdscr.addstr('\n')
