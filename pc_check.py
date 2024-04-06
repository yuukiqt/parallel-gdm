import socket
import os
import zipfile

import settings 

def get_ip_addr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()[0]

def result_dir():
    try:
        os.mkdir(os.getcwd() + r"\results")
    except FileExistsError:
        print('Folder results already created')

def unzip_data():    
    with zipfile.ZipFile('data.zip', 'r') as zip_ref:
        zip_ref.extractall()

pc_count = len(settings.workers) + len(settings.hosts)
