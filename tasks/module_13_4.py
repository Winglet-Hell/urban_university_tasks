import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

# Токен бота
BOT_TOKEN = "8170140420:AAHHaGBCjK22oQNtz515IWXrmvQg6re-X-Q"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


# Определение классов состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")


# Обработчик текстового сообщения 'Calories'
@dp.message(F.text.casefold() == "calories")  # Используем магический фильтр
async def calories_command(message: Message, state: FSMContext):
    await message.answer("Введите ваш возраст:")
    await state.set_state(UserState.age)


# Обработчик ввода возраста
@dp.message(UserState.age)  # Фильтр по состоянию
async def set_age(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        if age <= 0:
            raise ValueError
        await state.update_data(age=age)
        await message.answer("Введите ваш рост в см:")
        await state.set_state(UserState.growth)
    except ValueError:
        await message.answer(
            "Пожалуйста, введите корректный возраст (положительное число)."
        )


# Обработчик ввода роста
@dp.message(UserState.growth)
async def set_growth(message: Message, state: FSMContext):
    try:
        growth = int(message.text)
        if growth <= 0:
            raise ValueError
        await state.update_data(growth=growth)
        await message.answer("Введите ваш вес в кг:")
        await state.set_state(UserState.weight)
    except ValueError:
        await message.answer(
            "Пожалуйста, введите корректный рост (положительное число)."
        )


# Обработчик ввода веса
@dp.message(UserState.weight)
async def set_weight(message: Message, state: FSMContext):
    try:
        weight = int(message.text)
        if weight <= 0:
            raise ValueError
        await state.update_data(weight=weight)

        # Получение всех данных
        data = await state.get_data()
        age = data.get("age")
        growth = data.get("growth")
        weight = data.get("weight")

        # Формула Миффлина - Сан Жеора для женщин
        calories = 10 * weight + 6.25 * growth - 5 * age - 161

        # Отправка результата пользователю
        await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
        await state.clear()
    except ValueError:
        await message.answer(
            "Пожалуйста, введите корректный вес (положительное число)."
        )


# Обработчик всех других сообщений
@dp.message()
async def all_messages(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
