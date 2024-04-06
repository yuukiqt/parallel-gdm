import socket

import settings

def send_cmd_worker(ip,
                    port=settings.port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    message = "run"
    client_socket.sendall(message.encode())

    client_socket.close()