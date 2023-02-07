from curses import window, wrapper

from interfaceutils import draw_menu, draw_toolbar

__title__ = 'CyberAPP'


def main_menu(stdscr: window):
    stdscr.clear()
    draw_toolbar(stdscr, __title__)
    draw_menu(stdscr, ('Chat', 'Exit'))

    stdscr.refresh()
    return stdscr.getkey()


def chat_menu(stdscr: window):
    stdscr.clear()
    draw_toolbar(stdscr, __title__)
    draw_menu(stdscr, ('Server', 'Client', 'Exit'))

    stdscr.refresh()
    return stdscr.getkey()


def main(stdscr: window):
    key = main_menu(stdscr)

    if key == '1':
        key = chat_menu(stdscr)
        if key == '3':
            main(stdscr)


if __name__ == '__main__':
    wrapper(main)
