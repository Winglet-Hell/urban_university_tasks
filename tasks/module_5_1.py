class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверяем, существует ли указанный этаж
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            # Выводим номера этажей от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)


# Создание объектов класса House
h1 = House("ЖК Горский", 18)
h2 = House("Домик в деревне", 2)

# Вызов метода go_to для каждого объекта с произвольным числом
h1.go_to(5)  # Должен вывести числа от 1 до 5
h2.go_to(10)  # Должен вывести "Такого этажа не существует"
