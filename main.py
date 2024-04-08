from autogui import run_app, open_model, run_simulation, wait_simulation, save_res
from send_to_workers import send_cmd_worker
from pc_check import get_ip_addr, result_dir, unzip_data, clear_cache, kill_tnav
from file_server import load_fileserver
from file_client import send_files_to_host
from log_results import move_results_to_log, results_log_dir
from optimizer import optim
import settings

import time

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

def log_files():
    results_log_dir()
    move_results_to_log()

def pipeline():
    prep_process()
    if get_ip_addr() in settings.hosts:
        send_all_workers()
    start_process()
    send_res_files()

    if get_ip_addr() in settings.hosts:
        log_files()

    kill_tnav()
    clear_cache()

    if get_ip_addr() in settings.hosts:
        for worker in settings.workers:
            optim()
            time.sleep(4)
            send_files_to_host(worker)
    else:
        load_fileserver(get_ip_addr())

if __name__ == "__main__":
    pipeline()