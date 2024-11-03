# Декоратор для проверки, является ли число простым
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем функцию и сохраняем результат
        if result < 2:
            print("Составное")  # Если число меньше 2, оно не простое

        else:
            # Проверяем делимость на числа от 2 до корня из результата
            for i in range(2, int(result**0.5) + 1):
                if result % i == 0:
                    print("Составное")  # Если делится, значит составное
                    break

            else:
                print("Простое")  # Если делителей нет, число простое
        return result  # Возвращаем результат

    return wrapper


# Функция для сложения трех чисел
@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)
