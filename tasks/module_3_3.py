def print_params(a=1, b="строка", c=True):
    print(a, b, c)


# Вызовы функции
print_params()  # 1 'строка' True
print_params(b=25)  # 1 25 True. По умолчанию ожидает строку, получает инт.
print_params(
    c=[1, 2, 3]
)  # 1 'строка' [1, 2, 3]. По умолчанию ожидает булл, получает лист (инт).


# Распаковка параметров
values_list = [100, "example", False]
values_dict = {"a": 3.14, "b": "dictionary", "c": True}

print_params(*values_list)  # 100 'example' False
print_params(**values_dict)  # 3.14 'dictionary' True

# Распаковка + отдельные параметры
values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)  # 54.32 'Строка' 42
