import matplotlib.pyplot as plt

# Создаем данные для графика
years = [2018, 2019, 2020, 2021, 2022]
values = [100, 150, 200, 250, 300]

# Строим линейный график
plt.plot(years, values, marker="o")
plt.title("Рост показателей по годам")
plt.xlabel("Год")
plt.ylabel("Значение")
plt.show()

# Строим столбчатую диаграмму
plt.bar(years, values, color="skyblue")
plt.title("Столбчатая диаграмма роста показателей")
plt.xlabel("Год")
plt.ylabel("Значение")
plt.show()
