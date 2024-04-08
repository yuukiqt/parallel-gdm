import socket
import time
import os

import settings
from pc_check import get_ip_addr

def send_files_to_host(host_ip=settings.hosts[0],
                       port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_ip, port))

    if host_ip in settings.hosts:
        filename = rf"results\sim_pc{(settings.hosts + settings.workers).index(get_ip_addr())}.txt"
    else:
        filename = rf"data\KR_var_1.INC"
    time.sleep(5) # delay for read file

    client_socket.send(filename.encode())

    with open(filename, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)
            
    if filename != "data\KR_var_1.INC" :
        os.remove(filename)
    print("File transfered.")
    
    client_socket.close()