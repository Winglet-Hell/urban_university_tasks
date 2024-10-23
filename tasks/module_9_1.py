def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Перебираем все переданные функции
    for func in functions:
        # Записываем результат работы функции под её названием
        results[func.__name__] = func(int_list)

    # Возвращаем словарь с результатами
    return results


# Проверка работы функции с примерами
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
