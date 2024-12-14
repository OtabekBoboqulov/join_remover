from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")


@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def handle_banned_member(message: types.Message):
    await message.delete()


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def handle_banned_member(message: types.Message):
    await message.delete()
