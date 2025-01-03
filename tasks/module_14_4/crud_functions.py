import sqlite3
import os


def initiate_db():
    db_path = os.path.join(
        "/Users/winglet/Documents/Study/urban_university_tasks/tasks/module_14_4",
        "products.db",
    )
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            image TEXT
        )
        """
    )

    # Проверка на наличие данных и добавление тестовых записей
    cursor.execute("SELECT COUNT(*) FROM Products")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            """
            INSERT INTO Products (title, description, price, image) 
            VALUES (?, ?, ?, ?)
            """,
            [
                (
                    "Спортивная бутылка",
                    "Для воды и напитков",
                    500,
                    "https://cdn1.ozone.ru/s3/multimedia-z/6119156147.jpg",
                ),
                (
                    "Фитнес-браслет",
                    "Удобный трекер активности",
                    2000,
                    "https://cdn1.ozone.ru/s3/multimedia-h/6062408789.jpg",
                ),
                (
                    "Йога-мат",
                    "Противоскользящий коврик",
                    1500,
                    "https://ir.ozone.ru/s3/multimedia-o/6656100396.jpg",
                ),
                (
                    "Скакалка",
                    "Для кардио тренировок",
                    300,
                    "https://avatars.mds.yandex.net/get-mpic/5221826/img_id4195852524146374497.jpeg/orig",
                ),
            ],
        )
    connection.commit()
    connection.close()


def get_all_products():
    db_path = os.path.join(
        "/Users/winglet/Documents/Study/urban_university_tasks/tasks/module_14_4",
        "products.db",
    )
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT id, title, description, price, image FROM Products")
    products = cursor.fetchall()

    connection.close()
    return products
