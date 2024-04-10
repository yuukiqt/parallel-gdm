import numpy as np

def create_file(SW_lab, Krw_lab, Kro_lab, sample_params):

    x1, n0, x2, nw = sample_params

    x1 = round(x1, 2)
    n0 = int(n0)
    x2 = round(x2, 2)
    nw = int(nw)

    print(x1, n0, x2, nw)

    Sor = 1 - SW_lab[Kro_lab.index(0)]
    Swc = SW_lab[Krw_lab.index(0)]

    Kro_model = []
    Krw_model = []

    for item in SW_lab:

        kro_item = round(max(0, x1*(((1 - item - Sor)/(1 - Swc - Sor))**n0)), 6)
        krw_item = round(max(0, x2*(((item - Swc)/(1 - Swc - Sor))**nw)), 6)

        if isinstance(kro_item, complex):
           Kro_model.append(0)
        else:
           Kro_model.append(kro_item)

        if isinstance(krw_item, complex):
           Krw_model.append(0)
        else:
           Krw_model.append(krw_item)

    return Kro_model, Krw_model

def generate_unique_uniform_samples_lists(param_ranges, n_samples):
    samples = []

    while len(samples) < n_samples:
        sample = tuple([np.random.uniform(low, high) for low, high in param_ranges])
        if sample not in samples:
            samples.append(sample)

    return samples


def get_files(param_ranges, n_samples, SW_lab, Krw_lab, Kro_lab):

    Kro_model_list = []
    Krw_model_list = []

    unique_samples_lists = generate_unique_uniform_samples_lists(param_ranges, n_samples)

    for sample_params in unique_samples_lists:

        Kro_model, Krw_model = create_file(SW_lab, Krw_lab, Kro_lab, sample_params)

        Kro_model_list.append(Kro_model)
        Krw_model_list.append(Krw_model)

    return Kro_model_list, Krw_model_list

def zero_after_first_zero(lst):
    zero_found = False
    for i in range(len(lst)):
        if zero_found:
            lst[i] = 0
        elif lst[i] == 0:
            zero_found = True
    return lst

def replace_columns_in_file(file_path, new_krw_values, new_kro_values, indx):
    """
    Заменяет второй и третий столбцы в строках с 4 по 16 файла формата INC.

    :param file_path: путь к исходному файлу INC.
    :param new_krw_values: новые значения для столбца Krw.
    :param new_kro_values: новые значения для столбца Kro.
    :return: путь к измененному файлу INC.
    """
    # Чтение исходного файла
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Проверка длин списков
    if len(new_krw_values) < 13 or len(new_kro_values) < 13:
        raise ValueError("Списки new_krw_values и new_kro_values должны содержать как минимум 13 элементов")

    # Форматирование и замена строк
    for i in range(3, 16):  # Обрабатываем строки с индексом от 4 до 16
        parts = lines[i].split()
        if len(parts) >= 4:
            parts[1] = str(new_krw_values[i-3])  # Заменяем Krw
            parts[2] = str(new_kro_values[i-3])  # Заменяем Kro
            lines[i] = '\t'.join(parts) + '\n'

    # Запись измененного файла
    with open(file_path, 'w') as file:
        file.writelines(lines)

    return file_path


def optim():
    param_ranges = [(0.7, 1), (1, 4), (0.5, 0.8), (1, 4)]
    n_samples = 1
    SW_lab = [0.07, 0.19, 0.25, 0.33, 0.42, 0.52, 0.54, 0.57, 0.59, 0.62, 0.63, 0.64]
    # значения фазовой проницаемости по воде
    Krw_lab = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # значения фазовой проницаемости по нефти
    Kro_lab = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]

    Kro_model_list, Krw_model_list = get_files(param_ranges, n_samples, SW_lab, Krw_lab, Kro_lab)

    file_path = 'data\KR_var_1.INC'
    with open(file_path, 'r') as file:
        num_data_lines = sum(1 for line in file if not line.startswith('/') and line.strip() and line.count('\t') >= 3)

    for i in range(len(Kro_model_list)):
        kro_values = zero_after_first_zero(Kro_model_list[i]) + [0]    
        krw_values = Krw_model_list[i] + [1]
        modified_file_path = replace_columns_in_file(file_path, krw_values, kro_values, i)
