from random import choice


# Lambda-функция для сравнения символов двух строк на совпадение
first = "Мама мыла раму"
second = "Рамена мало было"

result = list(map(lambda x, y: x == y, first, second))
print(result)


# Замыкание для записи данных в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "a") as file:
            for data in data_set:
                file.write(
                    str(data) + "\n"
                )  # Преобразуем всё к строке и добавляем переход на новую строку

    return write_everything


# Пример использования замыкания
write = get_advanced_writer("example.txt")
write("Это строчка", ["А", "это", "уже", "число", 5, "в", "списке"])

# Класс MysticBall с методом __call__, выбирающий случайное слово


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример использования MysticBall
first_ball = MysticBall("Да", "Нет", "Наверное")
print(first_ball())  # Вернёт случайное слово
print(first_ball())  # Вернёт случайное слово
print(first_ball())  # Вернёт случайное слово
