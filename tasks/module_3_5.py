def get_multiplied_digits(number):

    # Преобразуем число в строку
    str_number = str(number)

    # Получаем первую цифру числа
    first = int(str_number[0])

    # Выводим отладочную информацию
    print(f"Обработка числа: {number}, первая цифра: {first}")

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        result = first * get_multiplied_digits(int(str_number[1:]))

        # Выводим отладочную информацию о промежуточном результате
        print(
            f"Произведение для числа {number} = {first} * результат рекурсии "
            f"({int(str_number[1:])}) = {result}"
        )

        return result

    else:
        # Если осталась одна цифра, возвращаем её
        print(f"\nВозвращаем последнюю цифру: {first}")

        return first


# Пример использования
result_func = get_multiplied_digits(40203)
print(f"\nИтоговый результат: {result_func}")
