from fastapi import FastAPI, Path
from typing import Annotated

# Создаем объект приложения
app = FastAPI()


# Главная страница
@app.get("/")
def read_root():
    return {"message": "Главная страница"}


# Страница администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}


# Страницы пользователей с параметром в пути
@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[
        int, Path(..., ge=1, le=100, description="Enter User ID", example=1)
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# Страницы пользователей с передачей данных в пути
@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[
        str,
        Path(
            ...,
            min_length=5,
            max_length=20,
            description="Enter username",
            example="UrbanUser",
        ),
    ],
    age: Annotated[int, Path(..., ge=18, le=120, description="Enter age", example=24)],
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
