from app.backend.db import Base, engine
from app.models import Task, User


# Генерация всех таблиц
def create_tables():
    print("Создание таблиц...")
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы.")


if __name__ == "__main__":
    create_tables()
