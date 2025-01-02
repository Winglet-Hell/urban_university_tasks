import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")

    # Поднимаем 5 шаров
    for i in range(1, 6):
        # Задержка обратно пропорциональна силе
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i} шар")

    print(f"Силач {name} закончил соревнования")


async def start_tournament():
    # Создаём 3 задачи для разных силачей
    task1 = asyncio.create_task(start_strongman("Pasha", 3))
    task2 = asyncio.create_task(start_strongman("Denis", 4))
    task3 = asyncio.create_task(start_strongman("Apollon", 5))

    # Ждём, пока все задачи завершатся
    await task1
    await task2
    await task3


# Запускаем асинхронную функцию
asyncio.run(start_tournament())