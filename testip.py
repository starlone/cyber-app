import socket


def test_ip_port(ip, port):
    obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return obj_socket.connect_ex((ip, port))
