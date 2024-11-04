import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Имитируем время, которое гость проводит за столом
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            # Проверяем наличие свободного стола
            available_table = next(
                (table for table in self.tables if table.guest is None), None
            )
            if available_table:
                # Сажаем гостя за стол
                available_table.guest = guest
                guest.start()  # Запускаем поток гостя
                print(f"{guest.name} сел(-а) за стол номер {available_table.number}")
            else:
                # Добавляем гостя в очередь, если нет свободных столов
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(
            table.guest is not None for table in self.tables
        ):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        # Гость закончил и ушел
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None

                        # Проверяем, есть ли кто-то в очереди
                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()  # Запускаем поток гостя
                            print(
                                f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"
                            )
            time.sleep(1)


# Создаем столы
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guest_names = [
    "Maria",
    "Oleg",
    "Vakhtang",
    "Sergey",
    "Darya",
    "Arman",
    "Vitoria",
    "Nikita",
    "Galina",
    "Pavel",
    "Ilya",
    "Alexandra",
]

# Создаем гостей
guests = [Guest(name) for name in guest_names]

# Инициализируем кафе со столами
cafe = Cafe(*tables)

# Прибытие гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
