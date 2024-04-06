import os

# from optimizer import epoch_count

epoch_count = 1

def move_results_to_log():
    res_files = list(os.listdir(r"results"))
    for file in res_files:
        os.replace(rf"results\{file}", rf'results_log\{file[:-4]}_ep{epoch_count}{file[-4:]}')

def results_log_dir():
    try:
        os.mkdir('results_log')
    except FileExistsError:
        print('Folder [results_log] already created')