import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from crud_functions import initiate_db, get_all_products, add_user, is_included

# Замените на ваш токен
BOT_TOKEN = "8170140420:AAHHaGBCjK22oQNtz515IWXrmvQg6re-X-Q"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Инициализация базы данных
initiate_db()


# Определение классов состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


# Создание клавиатур
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рассчитать"),
            KeyboardButton(text="Информация"),
            KeyboardButton(text="Купить"),
            KeyboardButton(text="Регистрация"),
        ]
    ],
    resize_keyboard=True,
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Рассчитать норму калорий", callback_data="calories"
            )
        ],
        [InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")],
    ]
)


# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)


# Регистрация пользователя
@dp.message(F.text == "Регистрация")
async def sing_up(message: Message, state: FSMContext):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username, F.text)
async def set_username(message: Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
        return
    await state.update_data(username=username)
    await message.answer("Введите свой email:")
    await state.set_state(RegistrationState.email)


@dp.message(RegistrationState.email, F.text)
async def set_email(message: Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age, F.text)
async def set_age(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        if age <= 0:
            await message.answer("Возраст должен быть положительным числом.")
            return
        await state.update_data(age=age)

        data = await state.get_data()
        add_user(data["username"], data["email"], data["age"])

        await message.answer(
            "Регистрация завершена! Добро пожаловать, {username}".format(
                username=data["username"]
            )
        )
        await state.clear()
    except ValueError:
        await message.answer("Введите корректный возраст (число).")


# Обработчик кнопки "Рассчитать"
@dp.message(F.text == "Рассчитать")
async def calculate_menu(message: Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


# Обработчик кнопки "Формулы расчёта"
@dp.callback_query(F.data == "formulas")
async def get_formulas(call: CallbackQuery):
    await call.message.answer(
        "Формула Миффлина - Сан Жеора:\n"
        "Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n"
        "Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161"
    )
    await call.answer()


# Обработчик кнопки "Рассчитать норму калорий"
@dp.callback_query(F.data == "calories")
async def start_calorie_calculation(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите ваш пол (м/ж):")
    await state.set_state(UserState.gender)
    await call.answer()


# Обработчик ввода пола
@dp.message(UserState.gender, F.text)
async def set_gender(message: Message, state: FSMContext):
    gender = message.text.lower()
    if gender not in ["м", "ж"]:
        await message.answer(
            "Пожалуйста, введите 'м' для мужского пола или 'ж' для женского пола."
        )
        return
    await state.update_data(gender=gender)
    await message.answer("Введите ваш возраст:")
    await state.set_state(UserState.age)


# Обработчик ввода возраста
@dp.message(UserState.age, F.text)
async def set_age_for_calculation(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        if not (1 <= age <= 120):
            await message.answer("Возраст должен быть в диапазоне от 1 до 120 лет.")
            return
        await state.update_data(age=age)
        await message.answer("Введите ваш рост в см:")
        await state.set_state(UserState.growth)
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст (число).")


# Обработчик ввода роста
@dp.message(UserState.growth, F.text)
async def set_growth(message: Message, state: FSMContext):
    try:
        growth = int(message.text)
        if not (50 <= growth <= 300):
            await message.answer("Рост должен быть в диапазоне от 50 до 300 см.")
            return
        await state.update_data(growth=growth)
        await message.answer("Введите ваш вес в кг:")
        await state.set_state(UserState.weight)
    except ValueError:
        await message.answer("Пожалуйста, введите корректный рост (число).")


# Обработчик ввода веса
@dp.message(UserState.weight, F.text)
async def set_weight(message: Message, state: FSMContext):
    try:
        weight = int(message.text)
        if not (10 <= weight <= 500):
            await message.answer("Вес должен быть в диапазоне от 10 до 500 кг.")
            return
        await state.update_data(weight=weight)

        data = await state.get_data()
        gender = data.get("gender")
        age = data.get("age")
        growth = data.get("growth")
        weight = data.get("weight")

        # Формула Миффлина - Сан Жеора
        if gender == "м":
            calories = 10 * weight + 6.25 * growth - 5 * age + 5
        else:
            calories = 10 * weight + 6.25 * growth - 5 * age - 161

        await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
        await state.clear()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный вес (число).")


# Обработчик кнопки "Купить"
@dp.message(F.text == "Купить")
async def get_buying_list(message: Message):
    products = get_all_products()
    for product in products:
        product_id, title, description, price, image = product
        await message.answer_photo(
            photo=image,
            caption=f"Название: {title} | Описание: {description} | Цена: {price}",
        )
    await message.answer(
        "Выберите продукт для покупки:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=product[1], callback_data=f"product_buying_{product[1]}"
                    )
                ]
                for product in products
            ]
        ),
    )


# Обработчик выбора продукта
@dp.callback_query(F.data.startswith("product_buying_"))
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


# Обработчик кнопки "Информация"
@dp.message(F.text == "Информация")
async def information(message: Message):
    await message.answer(
        "Этот бот помогает рассчитать норму калорий на основе вашего пола, возраста, "
        "роста и веса. Также доступен функционал покупки товаров."
    )


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
