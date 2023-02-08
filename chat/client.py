# Echo client program
import socket


def start(host='localhost', port=5007):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = input("Enter a phrase to send to the server: ")

        s.sendall(message.encode())
        data = s.recv(1024)
    print('Received', repr(data))
