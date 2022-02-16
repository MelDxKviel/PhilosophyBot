import os
import logging

from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.environ["BOT_TOKEN"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет, я философский бот Сократ! Отправь мне имя или фамилию философа,"
                         " и я расскажу тебе о нем. Также ты можешь посмотреть его цитаты или список"
                         " трудов, нажав на соответствующие кнопки.")



def main() -> None:
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
