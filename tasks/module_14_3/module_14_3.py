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

# Замените на ваш токен
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
    gender = State()


# Создание клавиатур
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рассчитать"),
            KeyboardButton(text="Информация"),
            KeyboardButton(text="Купить"),
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

inline_buy_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Спортивная бутылка", callback_data="product_buying"
            )
        ],
        [InlineKeyboardButton(text="Фитнес-браслет", callback_data="product_buying")],
        [InlineKeyboardButton(text="Йога-мат", callback_data="product_buying")],
        [InlineKeyboardButton(text="Скакалка", callback_data="product_buying")],
    ]
)


# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)


# Обработчик кнопки "Рассчитать"
@dp.message(F.text == "Рассчитать")
async def main_menu(message: Message):
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
async def set_gender(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите ваш пол (м/ж):")
    await state.set_state(UserState.gender)
    await call.answer()


# Обработчик кнопки "Купить"
@dp.message(F.text == "Купить")
async def get_buying_list(message: Message):
    products = [
        {
            "name": "Спортивная бутылка",
            "description": "Для воды и напитков",
            "price": 500,
            "image": "https://cdn1.ozone.ru/s3/multimedia-z/6119156147.jpg",
        },
        {
            "name": "Фитнес-браслет",
            "description": "Удобный трекер активности",
            "price": 2000,
            "image": "https://cdn1.ozone.ru/s3/multimedia-h/6062408789.jpg",
        },
        {
            "name": "Йога-мат",
            "description": "Противоскользящий коврик",
            "price": 1500,
            "image": "https://ir.ozone.ru/s3/multimedia-o/6656100396.jpg",
        },
        {
            "name": "Скакалка",
            "description": "Для кардио тренировок",
            "price": 300,
            "image": "https://avatars.mds.yandex.net/get-mpic/5221826/img_id4195852524146374497.jpeg/orig",
        },
    ]

    for product in products:
        await message.answer_photo(
            photo=product["image"],
            caption=f"Название: {product['name']} | Описание: {product['description']} | Цена: {product['price']}",
        )
    await message.answer(
        "Выберите продукт для покупки:", reply_markup=inline_buy_keyboard
    )


# Обработчик выбора продукта
@dp.callback_query(F.data == "product_buying")
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


# Обработчик ввода пола
@dp.message(UserState.gender, F.text)
async def handle_gender(message: Message, state: FSMContext):
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
async def handle_age(message: Message, state: FSMContext):
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
async def handle_growth(message: Message, state: FSMContext):
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
async def handle_weight(message: Message, state: FSMContext):
    try:
        weight = int(message.text)
        if not (10 <= weight <= 500):
            await message.answer("Вес должен быть в диапазоне от 10 до 500 кг.")
            return
        await state.update_data(weight=weight)

        # Получение всех данных
        data = await state.get_data()
        age = data.get("age")
        growth = data.get("growth")
        weight = data.get("weight")
        gender = data.get("gender")

        # Формула Миффлина - Сан Жеора с учётом пола
        if gender == "м":
            calories = 10 * weight + 6.25 * growth - 5 * age + 5
        else:
            calories = 10 * weight + 6.25 * growth - 5 * age - 161

        # Отправка результата пользователю
        await message.answer(
            f"Ваша норма калорий: {calories:.2f} ккал.",
            reply_markup=keyboard,  # Возвращаем клавиатуру
        )
        await state.clear()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный вес (число).")


# Обработчик кнопки "Информация"
@dp.message(F.text == "Информация")
async def information(message: Message):
    await message.answer(
        "Этот бот помогает рассчитать норму калорий на основе вашего пола, возраста, роста и веса."
    )


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
