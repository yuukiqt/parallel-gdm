from autogui import run_app, open_model, run_simulation, wait_simulation, save_res
from send_to_workers import send_cmd_worker
from pc_check import get_ip_addr, result_dir, unzip_data, clear_cache
from file_server import load_fileserver
from file_client import send
import settings

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
        c_size = (settings.hosts + settings.workers).index(get_ip_addr())
        if c_size > 1:
            time.sleep(3)
        send_files_to_host()

def pipeline():
    prep_process()
    if get_ip_addr() in settings.hosts:
        send_all_workers()
    start_process()
    clear_cache()

if __name__ == "__main__":
    pipeline()