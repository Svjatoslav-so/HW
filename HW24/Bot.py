import os

from aiogram import Bot, Dispatcher, executor, types

from DBManager import BoatDB

TOKEN = os.environ['token']
DATABASE = os.environ['database']


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = BoatDB(DATABASE)


async def start(message: types.Message):
    db.add_user((message.from_user.id,
                 message.from_user.first_name,
                 message.from_user.last_name,
                 message.from_user.username))


dp.register_message_handler(start, commands="start")

if __name__ == '__main__':
    print("start")
    db.create_db()
    executor.start_polling(dp)
