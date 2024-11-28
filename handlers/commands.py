from aiogram import types, Dispatcher


async def start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}\nДобро Пожаловать в Магазин",
    )


async def info(message: types.Message):
    await message.reply(
        "Информация:\n"
        f"текуший пользователь: {message.from_user.first_name}\n"
        f"текуший юзер: {message.from_user.id}\n"
        f"версия бота: 1.0\n"
        f"бот для Интернет магазина kaami\n"
        f"все права защищены © 2024\n"
        f"{'-'*50}\n"
        f"консультация: @kaamitan\n"
        f"tg: @kaamitan\n"
        f"email: azibekovakamila@gmail.com\n"
        f"phone: +996 999 99-99-99\n"
    )


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(info, commands=["info"])
