from chat import client, server
from interfaceutils import clear, draw_menu, draw_toolbar, getch
from packet_sniffer.packet_sniffer import packet_sniffer
from scan import testip
from scan.bannergrabbing import banner_grabbing
from scan.scanports import scan

__title__ = 'CyberAPP'


def main_menu():
    clear()
    draw_toolbar(__title__)
    draw_menu(('Chat', 'Test IP and PORT', 'PortScan',
              'Banner Grabbing', 'Packet Sniffer'))
    return getch()


def chat_menu():
    clear()
    draw_toolbar(__title__ + ' - Chat')
    draw_menu(('Server', 'Client', 'Back'))
    return getch()


def chat_start_server():
    clear()
    draw_toolbar(__title__ + ' - Chat - Server')
    print()
    server.start()


def chat_start_client():
    clear()
    draw_toolbar(__title__ + ' - Chat - Client')
    client.start()


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


def portscan_menu():
    clear()
    draw_toolbar(__title__ + ' - PortScan')

    draw_menu(('Well-known ports', 'Registered ports'))
    key = getch()
    if key == '1':
        ports = range(1, 1024)
        scan_ports(ports)
    elif key == '2':
        ports = range(1024, 49151)
        scan_ports(ports)

    print('\n\nEnter any key to continue')
    return getch()


def scan_ports(ports):
    print("\nScanning ports...")
    result = scan('localhost', ports)
    print('Open ports: ')
    for i in result:
        if i['result'] == 0:
            print(i['host'] + ":" + str(i['port']))


def test_banner_grabbing():
    clear()
    draw_toolbar(__title__ + ' - Banner Grabbing')

    ip = input("IP: ")

    port = input("PORT: ")

    print("Result: ")
    result = banner_grabbing(ip, int(port))
    print(result)

    print('\n\nEnter any key to continue')
    return getch()


def print_packet_sniffer(resp):
    print("--------Ethernet Frame--------")
    print("desination mac", resp['mac']['dest'])
    print("Source mac", resp['mac']['source'])

    print("-----------IP------------------")
    print("Source IP", resp['ip']['source'])
    print("Destination IP", resp['ip']['dest'])


def test_packet_sniffer():
    clear()
    draw_toolbar(__title__ + ' - Packat Sniffer')

    try:
        packet_sniffer(print_packet_sniffer)
    except KeyboardInterrupt:
        print('\n\nKeyboard interrupt!')

    print('\n\nEnter any key to continue')
    return getch()


def main():
    key = main_menu()

    match key:
        case '1':
            key = chat_menu()
            if key == '1':
                chat_start_server()
            elif key == '2':
                chat_start_client()
            elif key == '3':
                main()
        case '2':
            test_ip_port()
            main()
        case '3':
            portscan_menu()
            main()
        case '4':
            test_banner_grabbing()
            main()
        case '5':
            test_packet_sniffer()
            main()


if __name__ == '__main__':
    main()
