# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {"Johnny", "Bilbo", "Steve", "Hendrick", "Aaron"}

# Упорядочить имена студентов
sorted_students = sorted(students)

# Вычислить средний балл и создать словарь

""" Чтобы выполнить это задание самострельно изучил работу циклов.
Также функций sum, len, enumerate. """

average_grades = {
    student: sum(grades[i]) / len(grades[i])
    for i, student in enumerate(sorted_students)
}

# Вывод результата
print(average_grades)
