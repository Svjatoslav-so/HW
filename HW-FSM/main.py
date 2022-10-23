import os

from aiogram import Bot, Dispatcher, executor, types

import keyboards as kb
from FSM import Storage

TOKEN = os.environ['token']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
state_storage = Storage()


@dp.message_handler(lambda m: state_storage.current_state(m.from_user.id) in (
        "add_filter", "name", "location", "min_price", "max_price"))
async def add_filter(message: types.Message):
    u_id = message.from_user.id
    text = "Выберите какие пункты фильтра вы хотите настроить, чтобы завершить жмите save_filter"
    if message.text == "boat_name":
        await message.answer("Введите название лодки:")
        state_storage.set_state(u_id, "name")
    elif message.text == "boat_location":
        await message.answer("Введите локацию лодки:")
        state_storage.set_state(u_id, "location")
    elif message.text == "boat_min_price":
        await message.answer("Введите минимальную цену лодки:")
        state_storage.set_state(u_id, "min_price")
    elif message.text == "boat_max_price":
        await message.answer("Введите максимальную цену лодки:")
        state_storage.set_state(u_id, "max_price")
    elif message.text == "save_filter":
        data = state_storage.get_data(u_id)
        if not (data is None):
            await message.answer(f"Ваш фильтр:\n{data}", reply_markup=kb.main_kb)
        else:
            await message.answer("Ваш фильтр пуст")
        state_storage.finish(u_id)
        state_storage.set_state(u_id, "main")
    else:
        if state_storage.current_state(u_id) == "name":
            state_storage.update_data(u_id, {"name": message.text})
        elif state_storage.current_state(u_id) == "location":
            state_storage.update_data(u_id, {"location": message.text})
        elif state_storage.current_state(u_id) == "min_price":
            state_storage.update_data(u_id, {"min_price": message.text})
        elif state_storage.current_state(u_id) == "max_price":
            state_storage.update_data(u_id, {"max_price": message.text})
        state_storage.set_state(u_id, "add_filter")
        await message.answer(text, reply_markup=kb.add_filter_kb)


@dp.message_handler(lambda m: state_storage.current_state(m.from_user.id) in ("calc", "X", "Y", "Operation"))
async def calculator(message: types.Message):
    chat_id = message.from_user.id
    if message.text == "main":
        await message.answer("Главное меню", reply_markup=kb.main_kb)
        state_storage.finish(chat_id)
        state_storage.set_state(chat_id, "main")
    else:
        if message.text == 'X':
            state_storage.set_state(chat_id, "X")
            text = 'Input X'
        elif message.text == 'Operation':
            state_storage.set_state(chat_id, "Operation")
            text = 'Input operator'
        elif message.text == 'Y':
            state_storage.set_state(chat_id, "Y")
            text = 'Input Y'
        else:
            if state_storage.current_state(chat_id) == "X":
                state_storage.update_data(chat_id, {"x": message.text})
            elif state_storage.current_state(chat_id) == "Operation":
                state_storage.update_data(chat_id, {"op": message.text})
            elif state_storage.current_state(chat_id) == "Y":
                state_storage.update_data(chat_id, {"y": message.text})
            state_storage.set_state(chat_id, "calc")
            data = state_storage.get_data(chat_id)
            if data is None:
                text = "Пример: x op y"
            else:
                text = f'{data.get("x")} {data.get("op")} {data.get("y")}'
        await bot.send_message(chat_id, text, reply_markup=kb.calc())
        print(f'{chat_id}-{message.from_user.username}', state_storage.get_data(chat_id))


@dp.message_handler(lambda m: state_storage.current_state(m.from_user.id) in ("main", None))
async def main(message: types.Message):
    u_id = message.from_user.id
    if message.text == "add_filter":
        state_storage.set_state(u_id, "add_filter")
        await message.answer("Создайте фильтр\nВыберите какие пункты фильтра вы хотите настроить,"
                             " чтобы завершить жмите save_filter", reply_markup=kb.add_filter_kb)
    elif message.text == "calc":
        state_storage.set_state(u_id, "calc")
        await message.answer("Калькулятор", reply_markup=kb.calc())
    else:
        await message.answer(f"{message.text} \nstate: {state_storage.current_state(u_id)}", reply_markup=kb.main_kb)


@dp.callback_query_handler()
async def call_echo(callback_q: types.CallbackQuery):
    print(callback_q)
    await bot.answer_callback_query(callback_q.id, text='qqqqqq')
    await bot.send_message(chat_id=callback_q.from_user.id, text=callback_q.data)


if __name__ == '__main__':
    executor.start_polling(dp)
