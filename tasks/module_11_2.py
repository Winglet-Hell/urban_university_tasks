def introspection_info(obj):
    # Получаем базовую информацию об объекте
    obj_type = type(obj).__name__
    obj_module = getattr(obj, "__module__", "Built-in")

    # Разделим атрибуты и методы
    attributes = []
    methods = []
    for item in dir(obj):
        if item.startswith("__") and item.endswith("__"):
            continue  # игнорируем магические методы для краткости
        attr = getattr(obj, item)
        if callable(attr):
            methods.append(item)
        else:
            attributes.append(item)

    # Формируем словарь с результатами
    info = {
        "type": obj_type,
        "module": obj_module,
        "attributes": attributes,
        "methods": methods,
    }
    return info


# Пример использования с числом
number_info = introspection_info(42)
print(number_info)


# Пример использования с классом
class Example:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


example_obj = Example("Alice")
example_info = introspection_info(example_obj)
print(example_info)
