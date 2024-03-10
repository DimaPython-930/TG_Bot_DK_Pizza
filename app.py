import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token='6613317533:AAGSJkzelDPIJyJzKAa20TicWOKkZs8sO2Q')

dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('It was the start command')

@dp.message()
async def echo(message: types.Message):
    text = message.text

    if text in ['Привет', 'привет', 'Hi', 'hi', 'Hello', 'hello']:
        await message.answer(f'{text} to you too')
    elif text in ['Пока', 'пока', 'Bye', 'bye']:
        await message.answer(f'{text} to you too')
    else:
        await message.answer(message.text)


async def main() -> None:
    await dp.start_polling(bot)

asyncio.run(main())
