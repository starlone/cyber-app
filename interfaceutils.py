from curses import A_REVERSE, window
from os import name, system


def draw_menu(items):
    for i, item in enumerate(items):
        print('{} - {}'.format(i + 1, item))


def draw_toolbar(text):
    print(text)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
