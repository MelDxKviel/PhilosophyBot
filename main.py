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


@dp.message_handler(commands=["admin"])
@auth
async def admin_menu(message: types.Message):
    await message.answer("Привет, админ!")

    # TODO: Добавить функционал добавлени философов, их цитат и трудов


@dp.message_handler()
async def search_philosopher(message: types.Message):
    data = get_philosopher(message.text.capitalize())
    if data is not None:
        bio = data[0]
        image_link = data[1]
        buttons = [
            types.InlineKeyboardButton(text="Цитаты", callback_data=f"quotes {data['id']}"),
            types.InlineKeyboardButton(text="Труды", callback_data=f"works {data['id']}"),
            types.InlineKeyboardButton(text="Википедия", url=data["wiki_link"])
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*buttons)
        await message.answer(f"{data['bio']}[.]({data['image_link']}", reply_markup=keyboard, parse_mode="Markdown")
    elif data is None:
        await message.answer("Философ не найден. Попробуйте ещё раз.")


def main() -> None:
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
