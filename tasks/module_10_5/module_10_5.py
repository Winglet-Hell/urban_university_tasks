import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        line = file.readline()
        while line:
            all_data.append(line.strip())
            line = file.readline()


if __name__ == "__main__":
    # Список имен файлов
    filenames = [f'/Users/winglet/Documents/Study/urban_university_tasks/tasks/module_10_5/file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print("Линейный вызов:", time.time() - start_time)

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print("Многопроцессный вызов:", time.time() - start_time)
