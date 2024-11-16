import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        место = 1
        while self.participants:
            for participant in list(self.participants):
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[место] = participant
                    место += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.__class__.all_results["test_usain_and_nick"] = {
            k: str(v) for k, v in result.items()
        }
        self.assertTrue(str(result[max(result)]) == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.__class__.all_results["test_andrey_and_nick"] = {
            k: str(v) for k, v in result.items()
        }
        self.assertTrue(str(result[max(result)]) == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.__class__.all_results["test_usain_andrey_and_nick"] = {
            k: str(v) for k, v in result.items()
        }
        self.assertTrue(str(result[max(result)]) == "Ник")


# Дополнительно: Исправление логической ошибки в Tournament

#     def start(self):
#         finishers = {}
#         место = 1
#         while self.participants:
#             for participant in sorted(self.participants, key=lambda x: -x.speed):
#                 participant.run()
#                 if participant.distance >= self.full_distance:
#                     finishers[место] = participant
#                     место += 1
#                     self.participants.remove(participant)
#
#         return finishers

if __name__ == "__main__":
    unittest.main()
