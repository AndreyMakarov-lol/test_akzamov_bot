import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from test_random_akzamov.test_main_random_akzamov import random_name

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7580307885:AAFFWdR9Y-LzzbhbZP9NIen2D5tY048mN7E")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Хэндлер на команду /random
#Возвращает имя рандомного файла из папки
@dp.message(Command("random"))
async def cmd_start(message: types.Message):
    await message.answer(random_name())

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())