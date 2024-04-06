import socket
import subprocess
import threading

from pc_check import get_ip_addr
import settings

def start_server(ip):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, settings.port))
    server_socket.listen(1)
    
    while True:
        client_socket, addr = server_socket.accept()

        if addr[0] in settings.hosts:
            threading.Thread(target=execute_script, args=(client_socket,)).start()
        else:
            client_socket.close()

def execute_script(client_socket):
    data = client_socket.recv(1024)
    if data:
        subprocess.run(["python", "main.py"])
    client_socket.close()

if __name__ == "__main__":
    if get_ip_addr() in settings.workers:
        start_server(get_ip_addr())
    else:
        print("Server not prepaired for launch")