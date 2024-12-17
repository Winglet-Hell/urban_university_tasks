import logging
import unittest
from module_12_4 import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    handlers=[logging.FileHandler("runner_tests.log", mode="w", encoding="utf-8")],
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            # Создаем объект с отрицательной скоростью
            runner = Runner("Вося", -5)
            runner.walk()  # Вызов walk для теста
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            # Создаем объект с некорректным типом для имени
            runner = Runner(123, 10)  # Передаем не строку
            runner.run()  # Вызов run для теста
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")


if __name__ == "__main__":
    unittest.main()
