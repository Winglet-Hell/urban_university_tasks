from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

# Токен бота
API_TOKEN = "8170140420:AAHHaGBCjK22oQNtz515IWXrmvQg6re-X-Q"

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.reply("Привет! Я бот, помогающий твоему здоровью.")


# Обработчик всех остальных сообщений
@dp.message()
async def all_messages(message: Message):
    await message.reply("Введите команду /start, чтобы начать общение.")


# Запуск бота
async def main():
    print("Бот запущен. Ожидаем сообщения...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
