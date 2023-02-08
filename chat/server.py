# Echo server program
import socket


def start(host='', port=5007):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print("Server started, waiting for connections... ({}:{})".format(host, port))
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print('Received', repr(data))
                if not data:
                    break
                conn.sendall(data)
