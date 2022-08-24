# Task 1

basketball_players = [
    {
        "full name": "Оскар Даниэл Безерра Шмидт",
        "growth": 205.0
    },
    {
        "full name": "Сергей Александрович Белов",
        "growth": 190.0
    },
    {
        "full name": "Джерри Алан Уэст",
        "growth": 188
    },
    {
        "full name": "Коби Бин Брайант",
        "growth": 198.0
    },
    {
        "full name": "Оскар Палмер Робертсон ",
        "growth": 196
    },
    {
        "full name": "Джон Хьюстон Стоктон ",
        "growth": 185.0
    },
    {
        "full name": "Карл Энтони Мэлоун",
        "growth": 206
    },
    {
        "full name": "Уильям Фелтон Билл Расселл ",
        "growth": 208.0
    },
    {
        "full name": "Уилтон Норман (Уилт) Чемберлен",
        "growth": 216
    },
    {
        "full name": "Майкл Джеффри Джордан",
        "growth": 198.0
    },
    {
        "full name": "Карим Абдул-Джаббар",
        "growth": 218
    }
]


def input_growth(prompt="\tВведите рост баскетболиста (см)\n"
                        ">>>>>>"):
    while True:
        try:
            growth = float(input(prompt))
            if not (150 < growth < 300):
                raise ValueError
            break
        except ValueError:
            print("\tНекорректные данные\n")
    return growth


def print_all():
    for player in basketball_players:
        for key, value in player.items():
            print(f"\t{key}: {value}")
        print()


def add_player():
    full_name = input("\tВведите ФИО баскетболиста\n"
                      ">>>>>>")
    growth = input_growth()
    basketball_players.append({"full name": full_name, "growth": growth})


def get_coincidence_list_by_name(name_list):
    for n_i in range(len(name_list)):
        name_list[n_i] = name_list[n_i].lower()
    coincidence_list = [0 * i for i in range(len(basketball_players))]
    was_find = False
    for i in range(len(basketball_players)):
        for key, value in basketball_players[i].items():
            if key == "full name":
                player_name = value.lower()
                for n in name_list:
                    if not (player_name.find(n) == -1):
                        was_find = True
                        coincidence_list[i] += 1
    return was_find, coincidence_list


def get_coincidence_list_by_growth(growth):
    coincidence_list = [0 * i for i in range(len(basketball_players))]
    was_find = False
    for i in range(len(basketball_players)):
        for key, value in basketball_players[i].items():
            if key == "growth" and value == growth:
                was_find = True
                coincidence_list[i] += 1

    return was_find, coincidence_list


def delete_player():
    name = input("\tВведите имя игрока, которого хотите удалить\n"
                 ">>>>>>")
    name_list = name.split()
    was_find, coincidence_list = get_coincidence_list_by_name(name_list)

    if not was_find:
        print("\tСовпадений не найдено")
    else:
        max_c = max(coincidence_list)
        while True:
            try:
                r_index = coincidence_list.index(max_c)
                remove = input(f"\tУдалить {basketball_players[r_index]['full name']} ? (y/n)\n"
                               ">>>>>>")
                if remove == "y" or remove == "у":  # первый - "игрек", второй - "у"
                    basketball_players.pop(r_index)
                    coincidence_list.pop(r_index)
                    print("\tИгрок успешно удален")
                else:
                    coincidence_list[r_index] = 0
            except ValueError:
                break


def find_player():
    while True:
        tag = input("\tДля поиска по имени введите: n\n"
                    "\tДля поиска по росту введите: g\n"
                    ">>>>>>")
        if tag == "n":
            name = input("\tВведите имя игрока, которого хотите найти\n"
                         ">>>>>>")
            name_list = name.split()
            was_find, coincidence_list = get_coincidence_list_by_name(name_list)
            break
        elif tag == "g":
            growth = input_growth("\tВведите рост игрока, которого хотите найти (см)\n"
                                  ">>>>>>")
            was_find, coincidence_list = get_coincidence_list_by_growth(growth)
            break
        else:
            print("\tНеразрешенное значение\n")

    if not was_find:
        print("\tСовпадений не найдено")
    else:
        max_c = max(coincidence_list)
        while True:
            try:
                f_index = coincidence_list.index(max_c)
                print(basketball_players[f_index])
                coincidence_list[f_index] = 0
            except ValueError:
                break


def change_player_growth():
    name = input("\tВведите имя игрока, чей рост хотите изменить\n"
                 ">>>>>>")
    name_list = name.split()
    was_find, coincidence_list = get_coincidence_list_by_name(name_list)
    if not was_find:
        print("\tСовпадений не найдено")
    else:
        max_c = max(coincidence_list)
        while True:
            try:
                r_index = coincidence_list.index(max_c)
                change = input(f"\tИзменить рост {basketball_players[r_index]['full name']}"
                               f" {basketball_players[r_index]['growth']}? (y/n)\n"
                               ">>>>>>")
                if change == "y" or change == "у":  # первый - "игрек", второй - "у"
                    growth = input_growth("\tВведите новый рост игрока\n"
                                          ">>>>>>")
                    basketball_players[r_index]["growth"] = growth
                    print("\tРост успешно изменен")
                coincidence_list[r_index] = 0
            except ValueError:
                break


commands_dict = {
    "print": print_all,
    "add": add_player,
    "del": delete_player,
    "find": find_player,
    "change": change_player_growth

}

while True:
    command = input("\nВведите команду:\n"
                    "\tprint - вывод на экран всех данных\n"
                    "\tadd   - добавить нового игрока в список\n"
                    "\tdel   - удалить игрока\n"
                    "\tfind  - поиск по имени или росту\n"
                    "\tchange- изменить рост игрока\n"
                    "\tquit  - завершение работы\n"
                    ">>>")
    if command == "quit":
        break
    try:
        commands_dict[command]()
    except KeyError:
        print("Команда не распознана")
