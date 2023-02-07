import curses
from curses import window, wrapper

import testip
from interfaceutils import draw_menu, draw_toolbar

__title__ = 'CyberAPP'


def main_menu(stdscr: window):
    stdscr.clear()
    draw_toolbar(stdscr, __title__)
    draw_menu(stdscr, ('Chat', 'Test IP and PORT'))
    stdscr.addstr('\n\nPress a menu number or any other key to exit')

    stdscr.refresh()
    return stdscr.getkey()


def chat_menu(stdscr: window):
    stdscr.clear()
    draw_toolbar(stdscr, __title__ + ' - Chat')
    draw_menu(stdscr, ('Server', 'Client', 'Back'))
    stdscr.addstr('\n\nPress a menu number or any other key to exit')

    stdscr.refresh()
    return stdscr.getkey()


def test_ip_port(stdscr: window):
    stdscr.clear()
    draw_toolbar(stdscr, __title__ + ' - Test IP and Port')
    curses.echo()

    stdscr.addstr("IP: ")
    ip = stdscr.getstr(20)

    stdscr.addstr("PORT: ")
    port = stdscr.getstr(5)

    stdscr.addstr("Result: ")
    result = testip.test_ip_port(ip, int(port))

    curses.noecho()

    if result == 0:
        stdscr.addstr("Available")
    else:
        stdscr.addstr("Unavailable")

    stdscr.addstr('\n\nPress any key to continue')

    stdscr.refresh()
    return stdscr.getkey()


def main(stdscr: window):
    key = main_menu(stdscr)

    match key:
        case '1':
            key = chat_menu(stdscr)
            if key == '3':
                main(stdscr)
        case '2':
            test_ip_port(stdscr)
            main(stdscr)


if __name__ == '__main__':
    wrapper(main)
