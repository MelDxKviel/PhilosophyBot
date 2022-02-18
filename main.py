import os
import logging

from aiogram import Bot, Dispatcher, executor, types

from db import get_philosopher

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_ID = os.environ["ADMIN_ID"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


def auth(func):
    async def wrapper(message):
        if message['from']['id'] != int(ADMIN_ID):
            return await message.reply("Вы не админ!", reply=False)
        return await func(message)

    return wrapper


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет, я философский бот Сократ! Отправь мне имя или фамилию философа,"
                         " и я расскажу тебе о нем. \n\nТакже ты можешь посмотреть его цитаты или список"
                         " трудов, нажав на соответствующие кнопки.")


@dp.message_handler()
async def search_philosopher(message: types.Message):
    bio = get_philosopher(message.text)
    if bio is not None:
        await message.answer(bio)
    elif bio is None:
        await message.answer("Философ не найден")


def main() -> None:
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
