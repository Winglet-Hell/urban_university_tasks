# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = "Победа команды Волшебники данных!"

# Использование оператора %

# Сценарий 1: Количество участников первой команды
team1_message = "В команде Мастера кода участников: %d!" % team1_num
print(team1_message)

# Сценарий 2: Количество участников в обеих командах
total_participants_message = "Итого сегодня в командах участников: %d и %d!" % (
    team1_num,
    team2_num,
)
print(total_participants_message)

# Использование метода format()

# Сценарий 3: Количество задач, решённых командой 2
score2_message = "Команда Волшебники данных решила задач: {}!".format(score_2)
print(score2_message)

# Сценарий 4: Время решения задач командой 2
time_message = "Волшебники данных решили задачи за {:.1f} с!".format(team2_time)
print(time_message)

# Использование f-строк

# Сценарий 5: Количество решённых задач по командам
score_message = f"Команды решили {score_1} и {score_2} задач."
print(score_message)

# Сценарий 6: Исход соревнования
result_message = f"Результат битвы: {challenge_result}"
print(result_message)

# Сценарий 7: Количество задач и среднее время решения
tasks_message = (
    f"Сегодня было решено {tasks_total} задач, "
    f"в среднем по {time_avg:.1f} секунды на задачу!"
)
print(tasks_message)
