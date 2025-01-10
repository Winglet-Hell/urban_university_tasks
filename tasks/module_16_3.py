from fastapi import FastAPI, HTTPException

app = FastAPI()

# Начальный словарь пользователей
users = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
def get_users():
    return users


@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    if age < 0:
        raise HTTPException(
            status_code=400, detail="Возраст должен быть неотрицательным числом."
        )

    # Найти следующий доступный ключ (максимальный + 1)
    new_user_id = str(max(map(int, users.keys())) + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"Пользователь {new_user_id} зарегистрирован"}


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if age < 0:
        raise HTTPException(
            status_code=400, detail="Возраст должен быть неотрицательным числом."
        )
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")

    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"Пользователь {user_id} обновлён"}


@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")

    del users[user_id]
    return {"message": f"Пользователь {user_id} удалён"}
