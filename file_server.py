import socket

import settings

def load_fileserver(host_ip=settings.host_ip[0],
                    port=12345):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host_ip, port))

    # Listen for incoming connections
    server_socket.listen()

    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established.")

    # Receive filename from client
    filename = client_socket.recv(1024).decode()
    print("Filename:", filename)

    # Open the file in binary mode
    with open(filename, 'wb') as file:
        # Receive file data in chunks and write to file
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print("File transfered.")

    # Close the client socket
    client_socket.close()

    # Close the server socket
    server_socket.close()
