import unittest


# Класс Runner для моделирования бегуна
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


# Тесты для проверки работы класса Runner
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("TestRunner1")
        for _ in range(10):
            runner.walk()
        # Ожидаемое значение distance после 10 шагов walk — 50
        self.assertEqual(
            runner.distance, 50, "Ожидалось, что дистанция будет 50 после 10 шагов."
        )

    def test_run(self):
        runner = Runner("TestRunner2")
        for _ in range(10):
            runner.run()
        # Ожидаемое значение distance после 10 шагов run — 100
        self.assertEqual(
            runner.distance,
            100,
            "Ожидалось, что дистанция будет 100 после 10 пробежек.",
        )

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Дистанции должны быть разными, так как используются разные методы
        self.assertNotEqual(
            runner1.distance,
            runner2.distance,
            "Дистанции должны отличаться после использования run и walk.",
        )

    # Тест с ошибкой
    def test_run_with_error(self):
        runner = Runner("ErrorTestRunner")
        for _ in range(10):
            runner.run()
        # Ошибочно ожидаем, что дистанция будет 90 после 10 пробежек
        self.assertEqual(
            runner.distance, 90, "Ожидалось, что дистанция будет 90 после 10 пробежек."
        )


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
