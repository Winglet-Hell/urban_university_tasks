import sqlite3

# Подключение к базе данных
db_path = "/Users/winglet/Documents/Study/urban_university_tasks/tasks/module_14_1/not_telegram.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Создание таблицы
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
"""
)

# Заполнение таблицы через цикл
for i in range(1, 11):
    username = f"User{i}"
    email = f"example{i}@gmail.com"
    age = i * 10
    balance = 1000
    cursor.execute(
        "INSERT INTO Users (id, username, email, age, balance) VALUES (?, ?, ?, ?, ?) "
        "ON CONFLICT(id) DO NOTHING",
        (i, username, email, age, balance),
    )

# Обновление каждой 2-й записи, начиная с 1-й
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

# Удаление каждой 3-й записи, начиная с 1-й
ids_to_delete = [i for i in range(1, 11, 3)]
cursor.executemany("DELETE FROM Users WHERE id = ?", [(id,) for id in ids_to_delete])

# Выборка записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()

# Вывод результатов
for username, email, age, balance in results:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Сохранение и закрытие соединения
conn.commit()
conn.close()
