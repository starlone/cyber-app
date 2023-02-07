import sys
import termios
import tty
from os import name, system


def draw_menu(items):
    for i, item in enumerate(items):
        print('{} - {}'.format(i + 1, item))
    print('\nEnter a menu number or any other key to exit')


def draw_toolbar(text):
    print(text)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())

    ch = sys.stdin.read(1)

    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
