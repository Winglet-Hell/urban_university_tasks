import sqlite3

# Путь к базе данных
db_path = "/Users/winglet/Documents/Study/urban_university_tasks/tasks/module_14_1/not_telegram.db"

# Подключение к базе данных
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Удаление записи с id = 6
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчёт общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

# Вычисление среднего баланса
average_balance = all_balances / total_users if total_users > 0 else 0

# Вывод среднего баланса
print(average_balance)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
