def all_variants(text):

    # Внешний цикл определяет начальный индекс подпоследовательности
    for start in range(len(text)):

        # Внутренний цикл определяет конечный индекс подпоследовательности
        for end in range(start + 1, len(text) + 1):

            # Генерируем подпоследовательность и возвращаем её с помощью yield
            yield text[start:end]


# Пример использования функции
a = all_variants("abc")
for i in a:
    print(i)
