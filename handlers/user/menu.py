from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.defoult import menu

@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer("Team", reply_markup=menu)

@dp.message_handler(Text(equals=["Real Madrid", "Barcelona", "Chelsea","Manchester United"]))
async def get_food(message: Message):
    await message.answer(f" {message.text}. Chosen", reply_markup=ReplyKeyboardRemove())