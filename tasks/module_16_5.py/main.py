from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pydantic import BaseModel

app = FastAPI()

# Инициализация шаблонов
templates = Jinja2Templates(directory="templates")

# Пустой список пользователей
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users}
    )


@app.get("/user/{user_id}")
def get_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    if age < 0:
        raise HTTPException(
            status_code=400, detail="Возраст должен быть неотрицательным числом."
        )

    new_user_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    if age < 0:
        raise HTTPException(
            status_code=400, detail="Возраст должен быть неотрицательным числом."
        )

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    raise HTTPException(status_code=404, detail="Пользователь не найден.")


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    raise HTTPException(status_code=404, detail="Пользователь не найден.")
