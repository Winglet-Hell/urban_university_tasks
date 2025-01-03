import sqlite3

# Создание и подключение к базе данных
conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()

# Создание таблицы Users
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

# Заполнение таблицы 10 записями
users_data = [
    (1, "User1", "example1@gmail.com", 10, 1000),
    (2, "User2", "example2@gmail.com", 20, 1000),
    (3, "User3", "example3@gmail.com", 30, 1000),
    (4, "User4", "example4@gmail.com", 40, 1000),
    (5, "User5", "example5@gmail.com", 50, 1000),
    (6, "User6", "example6@gmail.com", 60, 1000),
    (7, "User7", "example7@gmail.com", 70, 1000),
    (8, "User8", "example8@gmail.com", 80, 1000),
    (9, "User9", "example9@gmail.com", 90, 1000),
    (10, "User10", "example10@gmail.com", 100, 1000),
]

cursor.executemany(
    (
        "INSERT INTO Users (id, username, email, age, balance) VALUES (?, ?, ?, ?, ?) "
        "ON CONFLICT(id) DO NOTHING"
    ),
    users_data,
)

# Обновление balance у каждой 2ой записи начиная с 1ой
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

# Удаление каждой 3ей записи начиная с 1ой
cursor.execute("DELETE FROM Users WHERE id % 3 = 0")

# Выборка всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()

# Вывод результатов в консоль
for username, email, age, balance in results:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
