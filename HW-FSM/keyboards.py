from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

boat_name_btn = KeyboardButton("boat_name")
location_btn = KeyboardButton("boat_location")
min_price_btn = KeyboardButton("boat_min_price")
max_price_btn = KeyboardButton("boat_max_price")
save_filter_btn = KeyboardButton("save_filter")

add_filter_kb = ReplyKeyboardMarkup(resize_keyboard=True)
add_filter_kb.row(boat_name_btn, location_btn)
add_filter_kb.row(min_price_btn, max_price_btn)
add_filter_kb.row(save_filter_btn)

calc_btn = KeyboardButton("calc")
add_filter_btn = KeyboardButton("add_filter")

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.row(calc_btn, add_filter_btn)


def calc():
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.row(
        KeyboardButton('X'),
        KeyboardButton('Operation'),
        KeyboardButton('Y'),
    )
    menu.row(KeyboardButton("main"))
    return menu
