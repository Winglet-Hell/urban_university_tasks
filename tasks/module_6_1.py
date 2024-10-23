# Родительские классы Animal и Plant
class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False  # Не накормлено
        self.name = name  # Имя

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True  # Накормлено
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False  # Погибает


class Plant:
    def __init__(self, name):
        self.edible = False  # Несъедобное
        self.name = name  # Имя


# Наследники Mammal и Predator от Animal
class Mammal(Animal):
    pass  # Использует метод eat от Animal


class Predator(Animal):
    pass  # Использует метод eat от Animal


# Наследники Flower и Fruit от Plant
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Съедобное


# Создание объектов классов
a1 = Predator("Волк с Уолл-Стрит")
a2 = Mammal("Хатико")
p1 = Flower("Цветик семицветик")
p2 = Fruit("Заводной апельсин")

# Действия по заданию
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
