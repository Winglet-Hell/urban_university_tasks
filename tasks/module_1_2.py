num_homeworks = 12
hours_spent = 1.5
course_name = "Python"
average_time_per_homework = hours_spent / num_homeworks

# Вариант с переменными через запятую.
print(
    "Курс:",
    course_name,
    "всего задач:",
    num_homeworks,
    "затрачено часов:",
    hours_spent,
    "среднее время выполнения",
    average_time_per_homework,
    "часа.",
)

# Вариант с f-строками.
print(
    f"Курс: {course_name},"
    f"всего задач: {num_homeworks},"
    f"затрачено часов: {hours_spent},"
    f"среднее время выполнения {average_time_per_homework} часа."
)

# Вариант с конкатенацией строк.
print(
    "Курс: "
    + course_name
    + ", всего задач: "
    + str(num_homeworks)
    + ", затрачено часов: "
    + str(hours_spent)
    + ", среднее время выполнения "
    + str(average_time_per_homework)
    + " часа."
)
