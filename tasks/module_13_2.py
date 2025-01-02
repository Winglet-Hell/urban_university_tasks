from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

# Токен вашего бота
API_TOKEN = " "

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.reply("Привет! Я бот помогающий твоему здоровью.")


# Обработчик всех остальных сообщений
@dp.message()
async def all_messages(message: Message):
    print("Введите команду /start, чтобы начать общение.")
    await message.reply("Введите команду /start, чтобы начать общение.")


# Запуск бота
async def main():
    print("Бот запущен. Ожидаем сообщения...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())