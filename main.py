from autogui import run_app, open_model, run_simulation, wait_simulation, save_res
from send_to_workers import send_cmd_worker
from pc_check import get_ip_addr, result_dir, unzip_data, clear_cache, kill_tnav
from file_server import load_fileserver
from file_client import send_files_to_host
from log_results import move_results_to_log, results_log_dir
from optimizer import optim
import settings

import time
import argparse

def help():
    parser = argparse.ArgumentParser(description='GDM parallel.')
    parser.add_argument('--epoch', type=int, help='Count of launchs')
    args = parser.parse_args()
    return args.epoch

def prep_process():
    result_dir()
    unzip_data()

def send_all_workers():
    for worker in settings.workers:
        send_cmd_worker(worker)

def start_process():
    run_app()
    open_model()
    run_simulation()
    wait_simulation()
    save_res()

def send_res_files():
    if get_ip_addr() in settings.hosts:
        for conn in range(len(settings.workers)):
            load_fileserver()
    else:
        con = (settings.hosts + settings.workers).index(get_ip_addr())
        if con != 1:
            time.sleep((con-1)*8) # 8 sec delay
        send_files_to_host()

def send_files_to_workers():
    if get_ip_addr() in settings.hosts:
        for worker in settings.workers:
            optim()
            time.sleep(2)
            send_files_to_host(worker)
        optim()
    else:
        load_fileserver(get_ip_addr())

def log_files():
    results_log_dir()
    move_results_to_log(curr_epoch)

def pipeline():
    prep_process()
    
    if get_ip_addr() in settings.hosts:
        send_all_workers()
        
    send_res_files()

    start_process()
    send_res_files()

    if get_ip_addr() in settings.hosts:
        log_files()

    kill_tnav()

    send_files_to_workers()

    time.sleep(2)

if __name__ == "__main__":
    epoch = help()
    if get_ip_addr() in settings.hosts:
        curr_epoch = 1
        while curr_epoch <= epoch:
            pipeline()
            curr_epoch += 1
    else:
        pipeline()
    clear_cache()