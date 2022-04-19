from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboard.default import menu
@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Hello!Choose your favourite cartoons!",reply_markup=menu)
@dp.message_handler(Text(equals=["Barbi", "Sponge Bob Square Pants", "Bratz","My noisy house","Riley's first date","Smeshariki"]))
async def get_food(message:Message):
    await message.answer(f"Choosen {message.text}.Thanks for choosing",
                         reply_markup=ReplyKeyboardRemove())

