import socket


def banner_grabbing(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        if s.connect_ex((host, port)) == 0:
            s.connect((host, port))
            if port in (80, 443):
                message = 'GET /\r\n\r\n'.encode()
                s.sendall(message)
                banner = s.recv(4096)
            else:
                try:
                    banner = s.recv(1024)
                except TimeoutError:
                    # If timeout, try http
                    message = 'GET /\r\n\r\n'.encode()
                    s.sendall(message)
                    banner = s.recv(4096)
    finally:
        s.close()
    return banner
