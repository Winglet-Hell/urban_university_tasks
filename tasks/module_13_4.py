import asyncio
from aiogram import Bot, Dispatcher
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
async def start_command(message: Message, state: FSMContext):
    await message.answer("Введите ваш возраст:")
    await state.set_state(UserState.age)


# Обработчик ввода возраста
@dp.message(UserState.age)
async def set_age(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        await state.update_data(age=age)
        await message.answer("Введите ваш рост в см:")
        await state.set_state(UserState.growth)
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст (число).")


# Обработчик ввода роста
@dp.message(UserState.growth)
async def set_growth(message: Message, state: FSMContext):
    try:
        growth = int(message.text)
        await state.update_data(growth=growth)
        await message.answer("Введите ваш вес в кг:")
        await state.set_state(UserState.weight)
    except ValueError:
        await message.answer("Пожалуйста, введите корректный рост (число).")


# Обработчик ввода веса
@dp.message(UserState.weight)
async def set_weight(message: Message, state: FSMContext):
    try:
        weight = int(message.text)
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
        await message.answer("Пожалуйста, введите корректный вес (число).")


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
