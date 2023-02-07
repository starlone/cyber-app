from curses import window, wrapper

__title__ = 'CyberAPP'


def main_menu(stdscr: window):
    stdscr.clear()
    stdscr.addstr(__title__)
    stdscr.addstr('\n')
    stdscr.addstr('\n1 - Chat')
    stdscr.addstr('\n2 - Exit')
    stdscr.refresh()
    return stdscr.getkey()


def chat_menu(stdscr: window):
    stdscr.clear()
    stdscr.addstr(__title__)
    stdscr.addstr('\n')
    stdscr.addstr('\n1 - Server')
    stdscr.addstr('\n2 - Client')
    stdscr.addstr('\n3 - Back')
    stdscr.refresh()
    return stdscr.getkey()


def main(stdscr: window):
    key = main_menu(stdscr)

    if key == '1':
        key = chat_menu(stdscr)
        if key == '3':
            main(stdscr)


wrapper(main)
