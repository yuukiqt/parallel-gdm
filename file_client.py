import socket
import time

import settings
from autogui import resname

def send_files_to_host(host_ip=settings.host_ip[0],
               port=12345):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host_ip, port))

    # Get the filename to transfer
    filename = resname
    time.sleep(3)

    # Send the filename to the server
    client_socket.send(filename.encode())

    # Open the file in binary mode
    with open(filename, 'rb') as file:
        # Read file data in chunks and send to server
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)

    print("File sent successfully.")

    # Close the client socket
    client_socket.close()