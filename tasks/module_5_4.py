class House:
    houses_history = []  # Атрибут класса для хранения истории названий зданий

    def __new__(cls, *args, **kwargs):
        # Создаем новый объект и добавляем название в историю
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])  # args[0] — это название здания
        return instance

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

    def __eq__(self, other):
        # Проверяем, если other = House, то сравниваем количество этажей
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        # Увеличиваем количество этажей на значение value
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        # Работает так же, как __add__
        return self.__add__(value)

    def __iadd__(self, value):
        # Работает так же, как __add__
        return self.__add__(value)

    def __del__(self):
        # Метод вызывается при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")


# Пример кода:
h1 = House("ЖК Эльбрус", 10)
print(House.houses_history)
h2 = House("ЖК Акация", 20)
print(House.houses_history)
h3 = House("ЖК Матрёшки", 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
