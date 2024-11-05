import pandas as pd

# Читаем данные из CSV-файла
data = pd.read_csv(
    "/Users/winglet/Documents/Study/urban_university_tasks/tasks/module_11_1.py/sample_data.csv"
)

# Выводим первые 5 строк
print("Первые 5 строк данных:")
print(data.head())

# Выполняем базовый анализ данных
print("\nАнализ данных:")
print(data.describe())

# Считаем количество уникальных значений в каждом столбце
print("\nКоличество уникальных значений:")
print(data.nunique())
