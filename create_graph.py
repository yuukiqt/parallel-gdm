import pandas as pd
import os
import matplotlib.pyplot as plt

from pc_check import pc_count

def create_plot(epoch):
    file_path = "results_log"

    files = []

    for i in range(pc_count):
        for j in range(epoch):
            files.append(f"sim_pc{i}_ep{j+1}.txt")

    date2stb = {}

    plt.figure(figsize=(12, 8))

    for file in files:
        data = pd.read_csv(f'{file_path}/{file}', delimiter='\t', skiprows=1)

        # Переименование столбцов
        column_names = ["Type", "Step", "Date", "Days", "Oil Rate, stb/day", "Oil Rate (H), stb/day",
                        "Water Rate, stb/day", "Water Rate (H), stb/day"]
        data.columns = column_names

        # Фильтрация строк, где Type начинается с "P"
        data = data[(data['Type'].str.startswith('P')) & (data["Type"] != "PROD")]

        # Функция для безопасного преобразования в float
        def safe_convert_to_float(x):
            try:
                return float(x.replace('e+', 'E').replace('+', ''))
            except ValueError:
                return None

        # Преобразование столбцов
        for col in ["Oil Rate, stb/day", "Oil Rate (H), stb/day", "Water Rate, stb/day", "Water Rate (H), stb/day"]:
            data[col] = data[col].apply(safe_convert_to_float)

        # Удаление строк с непреобразуемыми значениями
        data = data.dropna(subset=["Oil Rate, stb/day", "Oil Rate (H), stb/day", "Water Rate, stb/day", "Water Rate (H), stb/day"])

        # Оставляем только нужные столбцы
        data = data[['Type', "Date", 'Step', 'Oil Rate, stb/day', 'Oil Rate (H), stb/day']]

        data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

        average_oil_rate = data.groupby('Date')[['Oil Rate, stb/day', 'Oil Rate (H), stb/day']].mean()

        date2stb[file] = {"Oil Rate, stb/day": average_oil_rate["Oil Rate, stb/day"].values.tolist(),
                            "Oil Rate (H), stb/day": average_oil_rate["Oil Rate (H), stb/day"].values.tolist(),
                            "Date": average_oil_rate.index.values.tolist()}

        if files[0] == file:
            plt.plot(date2stb[file]["Date"], date2stb[file]["Oil Rate (H), stb/day"], label='Моделирование исторических данных')
        plt.plot(date2stb[file]["Date"], date2stb[file]["Oil Rate, stb/day"], label=file[:-4])


    plt.xlabel('Дата')
    plt.ylabel('Y')
    plt.legend()
    plt.savefig("final_results.png")
    plt.close()