import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)  # условная блокировка
        self.withdraw_done = False  # флаг завершения снятия

    def deposit(self):
        while True:
            with self.condition:
                # Завершаем, если снятие больше не требуется
                if self.withdraw_done:
                    break

                # Пополняем баланс случайной суммой
                amount = random.randint(50, 500)
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")

                # Уведомляем поток снятия, если средства пополнились
                self.condition.notify_all()

            time.sleep(0.001)  # имитируем задержку

    def take(self):
        for _ in range(100):
            with self.condition:
                amount = random.randint(
                    50, 500
                )  # генерируем новый запрос в каждой итерации
                print(f"Запрос на {amount}")

                # Ожидаем, пока баланс не станет достаточным для снятия
                while amount > self.balance:
                    print(
                        "Запрос отклонён, недостаточно средств. Ожидание пополнения..."
                    )
                    self.condition.wait()
                    amount = random.randint(
                        50, 500
                    )  # генерируем новый запрос после ожидания

                # Когда баланс достаточен, снимаем средства
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")

        # Устанавливаем флаг завершения снятия после обработки всех запросов
        with self.condition:
            self.withdraw_done = True
            self.condition.notify_all()  # Уведомляем поток пополнения, что снятие завершено


# Создаем объект банка
bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f"Итоговый баланс: {bk.balance}")
