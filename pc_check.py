import socket
import os
import zipfile
import shutil

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
    if os.path.exists('data'):
        pass # insert new file after optimize
    else:
        with zipfile.ZipFile('data.zip', 'r') as zip_ref:
            zip_ref.extractall()

def clear_cache():
    shutil.rmtree('__pycache__')

pc_count = len(settings.workers) + len(settings.hosts)
