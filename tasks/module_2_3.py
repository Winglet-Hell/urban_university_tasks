# Создает список my_list.
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Выводит в консоль исходные данные.
print("\nИсходные данные:")
print("my_list =", my_list)

# Создает начальный индекс.
index = 0

# Вывод в консоль положительных чисел.
print("\nВывод на консоль:")
while index < len(my_list):
    if my_list[index] < 0:
        break
    elif my_list[index] > 0:
        print(my_list[index])
    index += 1
