class WordsFinder:
    def __init__(self, *file_names):
        # Записываем имена файлов в атрибут
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        # Перебираем файлы и извлекаем слова
        for file_name in self.file_names:
            with open(file_name, "r", encoding="utf-8") as file:
                text = file.read().lower()  # Приводим к нижнему регистру
                # Убираем пунктуацию
                for punct in [",", ".", "=", "!", "?", ";", ":", " - "]:
                    text = text.replace(punct, " ")
                words = text.split()  # Разбиваем текст на слова
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()  # Игнорируем регистр
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            if word in words:
                result[name] = (
                    words.index(word) + 1
                )  # Возвращаем позицию первого вхождения
            else:
                result[name] = -1  # Если слова нет, возвращаем -1
        return result

    def count(self, word):
        word = word.lower()  # Игнорируем регистр
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            result[name] = words.count(word)  # Считаем количество вхождений
        return result


# Пример использования
finder = WordsFinder(
    "/Users/winglet/Yandex.Disk.localized/Study/urban_university/tasks/"
    "module_7_3/test_file.txt"
)
print(finder.get_all_words())  # Все слова
print(finder.find("TEXT"))  # Поиск слова 'TEXT'
print(finder.count("teXT"))  # Подсчёт слова 'teXT'
