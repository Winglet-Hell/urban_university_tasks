import threading
from time import sleep, time


# Определение функции для записи в файл
def write_words(word_count, file_name):
    with open(file_name, "w") as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды между записями
    print(f"Завершилась запись в файл {file_name}")


# Основной блок кода
if __name__ == "__main__":
    # Запуск функций в однопоточном режиме
    start_time = time()
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")
    end_time = time()
    print(f"Работа функций заняла: {end_time - start_time:.6f} секунд")

    # Создание потоков
    threads = [
        threading.Thread(target=write_words, args=(10, "example5.txt")),
        threading.Thread(target=write_words, args=(30, "example6.txt")),
        threading.Thread(target=write_words, args=(200, "example7.txt")),
        threading.Thread(target=write_words, args=(100, "example8.txt")),
    ]

    # Запуск потоков и замер времени
    start_time = time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time()
    print(f"Работа потоков заняла: {end_time - start_time:.6f} секунд")
