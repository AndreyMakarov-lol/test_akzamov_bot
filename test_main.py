import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile
from aiogram.filters.command import Command
from test_random_akzamov.test_main_random_akzamov import random_name

#Преобразуем путь к файлу в вид который нравиться библиотеке
def random_img_path():
    all_file_path = FSInputFile(random_name('test_dir'))
    return all_file_path


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7580307885:AAFFWdR9Y-LzzbhbZP9NIen2D5tY048mN7E")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Кекный Акзамов")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, input_field_placeholder="Нажми и получишь Акзамова")
    await message.answer("Привет! Хочешь кекного акзвмова?", reply_markup=keyboard )



@dp.message(F.text.lower() == "кекный акзамов")
async def with_puree(message: types.Message):
    await message.answer_photo(random_img_path())







# # Хэндлер на команду /random
# #Возвращает имя рандомного файла из папки
# @dp.message(Command("random"))
# async def cmd_random(message: types.Message):
#     await message.answer_photo(random_img_path())

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())