import os
import sys
import termios
import tty


def draw_menu(items):
    for i, item in enumerate(items):
        print('{} - {}'.format(i + 1, item))
    print('\nEnter a menu number or any other key to exit')


def draw_toolbar(text):
    # Get the size of the terminal
    size = os.get_terminal_size().columns
    line = '-' * size
    print(line)
    print(text)
    print(line)
    print()


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())

    ch = sys.stdin.read(1)

    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
