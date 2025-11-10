# bot.py
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Напиши что-нибудь — я повторю.")

@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

if __name__ == "__main__":
    import asyncio
    print("Бот запускается...")
    asyncio.run(dp.start_polling(bot))
