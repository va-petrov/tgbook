from asyncio import sleep

from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterDocument

# Use your own values from my.telegram.org
api_id = 4960103
api_hash = '1c30e5f7b5b29f321f89cb1dcba887aa'

ignore_dialogs = [
    "Лучшее с Aliexpress",
    "AliExpress",
    "AliOffPrice | AliExpress, Купоны, Промокоды",
    "Товары с АлиЭкспресс",
    "Что купить на AliExpress?",
    "Топ AliExpress",
    "AliExpress для мужиков",
    "ПК с Aliexpress",
    "Xiaomi | Сяоми | Гаджеты | Смартфоны",
    "SPb Python Drinkup & Bar Hopping",
    "AliExpress на скидках",
    "BZD • ЧАТ",
    "Sci-Hub",
    "Selectel Newsfeed",
    "SPb 3D Orders",
    "Посылки из Китая",
    "Учимся дома: официальная информация для родителей и школьников Санкт-Петербурга",
    "AliExpress | Черная Пятница Купоны▫️Гаджеты▫️Смартфоны▫️Китай▫️Лайфхаки▫️Шоппинг▫️Такси▫️Технологии▫️Подарки",
    "Сергей Голубев (Ленинград)",
    "Алексей Ягунов",
    "Vladimir K",
    "Юрий Носов",
    "Невский Проспект Галина",
    "Петр Петров",
    "СЕВЕР-СВ 2.0",
    "🖥 JuniorProger 🖥",
    "Py Books",
    "Alexander",
    "SLA",
    "Стас Высоцкий",
    "RoboDIY_ru",
    "Олег Барсуков",
    "Алена Барсукова, Ленинград",
    "Студия - бухгалтерия",
    "Алиса Селезнёва",
    "HRity (Эйчарити)",
    "Сергей Мелентьев",
    "Max Efmv",
    "_NORTH_",
    "Студия - руководство",
    "Timur Gudkov",
    "Евгений",
    "Максим Бравцев",
    "Anna Egorova (Ivaniy)",
    "Володя Мастер",
    "Фауст",
    "Vladimir",
    "PhKis Pavel Shelishch",
    "Божественная комедия",
    "Дмитрий Мишин",
    "Борис Любимов",
    "Хуршид",
    "Алексей Галанов"
]

async def main():
    # Getting information about yourself
    # me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs(ignore_pinned=True, archived=True):
    #    # print(dialog.name, 'has ID', dialog.id)
    #     print('"'+dialog.name+'",')

    while True:
        async for dialog in client.iter_dialogs(ignore_pinned=True, archived=True):
            if dialog.name not in ignore_dialogs and dialog.unread_count>0:
                async for message in client.iter_messages(dialog.id):
                    print(dialog.name, message.id)
                    await message.mark_read()
                    break

        print('===========================')
        await sleep(60)

    # You can print the message history of any chat:
    # async for message in client.iter_messages('Архив журналов (1890-2021)', filter=InputMessagesFilterDocument):
    #     if message.file:
    #         # print(message)
    #         print(message.file.name, message.file.size)
    #         await message.mark_read()
    #         # path = await message.download_media(message.file.name)
    #         # print(path)
    #         break
    #     else:
    #         print('!')


# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(main())