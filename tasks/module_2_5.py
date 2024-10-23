def get_matrix(n, m, value):
    # Создаем пустую матрицу
    matrix = []

    # Внешний цикл для добавления строк
    for _ in range(n):
        # Создаем строку матрицы
        row = []

        # Внутренний цикл для добавления значений в строку
        for _ in range(m):
            row.append(value)

        # Добавляем строку в матрицу
        matrix.append(row)

    # Возвращаем готовую матрицу
    return matrix


# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(5, 2, 555)

# Вывод результата
print(result1)
print(result2)
print(result3)
print(result4)
