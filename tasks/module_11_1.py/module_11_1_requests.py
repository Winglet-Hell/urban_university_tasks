import requests

# Отправляем GET-запрос к API для получения данных
response = requests.get("https://api.github.com")
print(f"Status Code: {response.status_code}")

# Если запрос успешен, извлекаем JSON-данные
if response.status_code == 200:
    data = response.json()
    print("Полученные данные:")
    print(data)
else:
    print("Не удалось получить данные.")
