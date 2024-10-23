# Глобальная переменная для подсчета вызовов
calls = 0


# Функция для подсчета вызовов других функций
def count_calls():
    global calls
    calls += 1


# Функция для обработки строки
def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    return len(string), string.upper(), string.lower()


# Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search


# Примеры вызова функций
print("\nПримеры вызова функций:")
print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban", ["ban", "BaNaN", "urBAN"]))
print(is_contains("cycle", ["recycling", "cyclic"]))

# Вывод количества вызовов функций
print(f"\nОбщее количество вызовов функций: {calls}")
