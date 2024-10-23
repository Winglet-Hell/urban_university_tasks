# Класс исключения для некорректного VIN номера
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        # Инициализация с атрибутом message для сообщения об ошибке
        self.message = message


# Класс исключения для некорректных автомобильных номеров
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        # Инициализация с атрибутом message для сообщения об ошибке
        self.message = message


# Основной класс Car
class Car:
    def __init__(self, model, vin, numbers):
        # Атрибут модели автомобиля
        self.model = model
        # Проверка и установка vin номера через приватный метод __is_valid_vin
        if self.__is_valid_vin(vin):
            self.__vin = vin
        # Проверка и установка номера автомобиля через приватный метод
        # __is_valid_numbers
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    # Приватный метод для проверки валидности VIN номера
    def __is_valid_vin(self, vin_number):
        # Проверка, что vin_number - целое число
        if not isinstance(vin_number, int):
            # Если не целое число, выбрасываем исключение IncorrectVinNumber
            raise IncorrectVinNumber("Некорректный тип vin номера")
        # Проверка, что vin_number находится в диапазоне от 1000000 до 9999999
        if not (1000000 <= vin_number <= 9999999):
            # Если vin_number не в указанном диапазоне,
            # выбрасываем исключение IncorrectVinNumber
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        # Если все проверки пройдены, возвращаем True
        return True

    # Приватный метод для проверки валидности автомобильных номеров
    def __is_valid_numbers(self, numbers):
        # Проверка, что numbers является строкой
        if not isinstance(numbers, str):
            # Если не строка, выбрасываем исключение IncorrectCarNumbers
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        # Проверка, что длина номера составляет ровно 6 символов
        if len(numbers) != 6:
            # Если длина номера не равна 6 символам,
            # выбрасываем исключение IncorrectCarNumbers
            raise IncorrectCarNumbers("Неверная длина номера")
        # Если все проверки пройдены, возвращаем True
        return True


# Пример использования программы
try:
    # Создаем объект first с корректными VIN и номерами
    first = Car("Model1", 1000000, "f123dj")
except IncorrectVinNumber as exc:
    # Если VIN некорректен, выводим сообщение об ошибке
    print(exc.message)
except IncorrectCarNumbers as exc:
    # Если номера некорректны, выводим сообщение об ошибке
    print(exc.message)
else:
    # Если исключений не возникло, выводим сообщение об успешном создании автомобиля
    print(f"{first.model} успешно создан")

try:
    # Пытаемся создать объект second с некорректным VIN (меньше диапазона)
    second = Car("Model2", 300, "т001тр")
except IncorrectVinNumber as exc:
    # Если VIN некорректен, выводим сообщение об ошибке
    print(exc.message)
except IncorrectCarNumbers as exc:
    # Если номера некорректны, выводим сообщение об ошибке
    print(exc.message)
else:
    # Если исключений не возникло, выводим сообщение об успешном создании автомобиля
    print(f"{second.model} успешно создан")

try:
    # Пытаемся создать объект third с корректным VIN, но некорректными номерами
    third = Car("Model3", 2020202, "нет номера")
except IncorrectVinNumber as exc:
    # Если VIN некорректен, выводим сообщение об ошибке
    print(exc.message)
except IncorrectCarNumbers as exc:
    # Если номера некорректны, выводим сообщение об ошибке
    print(exc.message)
else:
    # Если исключений не возникло, выводим сообщение об успешном создании автомобиля
    print(f"{third.model} успешно создан")
