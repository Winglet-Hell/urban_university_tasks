import unittest
from functools import wraps
from module_12_2 import Runner, Tournament

# Декоратор для контроля выполнения тестов


def skip_if_frozen(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cls = args[0].__class__
        if getattr(cls, "is_frozen", False):
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return func(*args, **kwargs)

    return wrapper


# Класс RunnerTest с добавлением проверки is_frozen


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("Test Runner", speed=5)

    @skip_if_frozen
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)

    @skip_if_frozen
    def test_challenge(self):
        self.runner.run()
        self.runner.walk()
        self.assertEqual(self.runner.distance, 15)


# Класс TournamentTest с добавлением проверки is_frozen


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(50, self.usain, self.nick)
        result = tournament.start()
        self.assertEqual(str(result[1]), "Усэйн")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.assertEqual(str(result[2]), "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.assertEqual(str(result[1]), "Усэйн")


# Создание TestSuite и добавление тестов


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(RunnerTest))
    test_suite.addTest(unittest.makeSuite(TournamentTest))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
