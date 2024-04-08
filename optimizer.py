import pandas as pd
import random

def optim():
    with open('data\KR_var_1.INC', 'r') as file:
        lines = file.readlines()

    data_lines = []
    start = False
    for line in lines:
        if line.startswith('--'):
            start = True
            continue
        if line.startswith('/'):
            break
        if start and line.strip():
            data_lines.append(line.strip())

    df = pd.DataFrame([line.split() for line in data_lines], columns=['SW', 'Krw', 'Kro', 'Pc'])

    df = df.astype(float)

    df.loc[1, ['SW', 'Krw']] = [random.uniform(0.078, 0.32), random.uniform(0,0.024)]

    previous_row = df.iloc[10]
    random_value1 = random.uniform(previous_row['SW'], 0.99)
    random_value2 = random.uniform(previous_row['Krw'], 0.99)

    df.loc[11, ['SW', 'Krw']] = [random_value1, random_value2]

    df = df.round(6)

    with open(r'data\KR_var_1.INC', 'w') as file:
        file.write("SWOF\n\n--SW\tKrw\tKro\tPc\n")
        for index, row in df.iterrows():
            file.write(f"{row['SW']}\t{row['Krw']}\t{row['Kro']}\t{row['Pc']}\n")
        file.write("/\n")