import testip
from chat import client, server
from interfaceutils import clear, draw_menu, draw_toolbar, getch

__title__ = 'CyberAPP'


def main_menu():
    clear()
    draw_toolbar(__title__)
    draw_menu(('Chat', 'Test IP and PORT'))
    return getch()


def chat_menu():
    clear()
    draw_toolbar(__title__ + ' - Chat')
    draw_menu(('Server', 'Client', 'Back'))
    return getch()


def test_ip_port():
    clear()
    draw_toolbar(__title__ + ' - Test IP and Port')

    ip = input("IP: ")

    port = input("PORT: ")

    print("Result: ")
    result = testip.test_ip_port(ip, int(port))

    if result == 0:
        print("Available")
    else:
        print("Unavailable")

    print('\n\nEnter any key to continue')
    return getch()


def main():
    key = main_menu()

    match key:
        case '1':
            key = chat_menu()
            if key == '1':
                server.start()
            elif key == '2':
                client.start()
            elif key == '3':
                main()
        case '2':
            test_ip_port()
            main()


if __name__ == '__main__':
    main()
