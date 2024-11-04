import time
from threading import Thread


class Knight(Thread):
    enemies = 100  # Общее количество врагов для всех рыцарей

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        while Knight.enemies > 0:
            time.sleep(1)  # Задержка на 1 секунду (1 день)
            self.days += 1
            Knight.enemies -= self.power
            if Knight.enemies < 0:
                Knight.enemies = 0
            print(
                f"{self.name} сражается {self.days} день(дня)..., осталось {Knight.enemies} воинов."
            )

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание рыцарей и запуск потоков
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидание окончания сражения всех рыцарей
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
