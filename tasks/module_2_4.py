# v.1 без отладочных выводов в консоль.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("\nv.1")

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем список numbers
for num in numbers:
    if num < 2:
        # Пропускаем 1 и числа меньше 2, потому что они не являются простыми
        continue

    is_prime = True  # Флаг, показывающий, является ли число простым

    # Проверяем делимость числа на все числа от 2 до квадратного корня из num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # Добавляем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки простых и не простых чисел
print("\nPrimes:", primes)
print("Not Primes:", not_primes)


# v.2 c отладочными выводами в консоль
# (помогли мне разобраться как работают циклы)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("\nv.2")

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем список numbers
for num in numbers:
    if num < 2:
        print(f"\nЧисло {num} пропущено, так как оно меньше 2 и не является простым.")
        continue

    is_prime = True  # Флаг, показывающий, является ли число простым

    print(f"\nПроверяем число: {num}")

    # Проверяем делимость числа на все числа от 2 до корня из num
    for i in range(2, int(num**0.5) + 1):
        print(f"  Проверяем делимость на {i}...")
        if num % i == 0:
            print(f"  {num} делится на {i}. Это составное число.")
            is_prime = False
            break  # Прерываем цикл, так как число уже не может быть простым

    # Добавляем число в соответствующий список
    if is_prime:
        print(f"  {num} - простое число, добавляем в список primes.")
        primes.append(num)
    else:
        print(f"  {num} - составное число, добавляем в список not_primes.")
        not_primes.append(num)

# Выводим списки простых и не простых чисел
print("\nРезультаты проверки:")
print("Primes:", primes)
print("Not Primes:", not_primes)
