import socket

import settings

def load_fileserver(host_ip=settings.hosts[0],
                    port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host_ip, port))

    server_socket.listen()

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    filename = client_socket.recv(1024).decode()
    print("Filename:", filename)

    with open(filename, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
    print("File downloaded.")

    client_socket.close()
    server_socket.close()