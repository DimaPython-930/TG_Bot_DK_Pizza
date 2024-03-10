import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('It was the start command')


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
