from fastapi import FastAPI, Query

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
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# Страницы пользователей с передачей данных в адресной строке
@app.get("/user")
def read_user_info(
    username: str = Query(..., description="Имя пользователя"),
    age: int = Query(..., description="Возраст пользователя"),
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
