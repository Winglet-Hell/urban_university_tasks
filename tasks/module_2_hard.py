def find_password(n):
    password = ""
    used_pairs = set()  # Создаем множество, чтобы избежать дублирования пар

    print(f"\nИщем пары чисел, сумма которых делится на {n}:")

    for i in range(1, 20):
        for j in range(i + 1, 20):
            pair_sum = i + j
            print(f"\nПара: ({i}, {j}), их сумма: {pair_sum}")

            if n % pair_sum == 0 and (i, j) not in used_pairs:
                print(
                    f"Число {n} делится на {pair_sum} без остатка. "
                    f"Добавляем пару в пароль."
                )
                password += str(i) + str(j)
                used_pairs.add((i, j))
            else:
                print(f"Число {n} НЕ делится на {pair_sum} без остатка.")

    return password


# Пример использования:
input_number = int(input("\nВведите число от 3 до 20: "))
result = find_password(input_number)
print(f"\nНужный пароль: {result}")
