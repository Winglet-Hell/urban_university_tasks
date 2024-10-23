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

    def __len__(self):
        # Возвращает количество этажей здания
        return self.number_of_floors

    def __str__(self):
        # Возвращает строку с информацией о здании
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# Создание объектов класса House
h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
