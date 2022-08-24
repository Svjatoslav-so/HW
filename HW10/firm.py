# Task 3
import re

firm = [
    {
        "full name": "Abhimanyu Gartia",
        "phone number": "22372849",
        "email": "gartia@posoco.in",
        "position": "Executive Director",
        "cabinet number": 13,
        "skype": "abhimanyu-gar13"
    },
    {
        "full name": "Somara Lakra",
        "phone number": "22235673",
        "email": "somara.lakra@posoco.in",
        "position": "Manager",
        "cabinet number": 23,
        "skype": "somara-lak23"
    },
    {
        "full name": "Anusha Baruah",
        "phone number": "22352850",
        "email": "anusha@posoco.in",
        "position": "Manager",
        "cabinet number": 27,
        "skype": "anusha-bar27"
    },
    {
        "full name": "Hirak Roy",
        "phone number": "22263463",
        "email": "hirakroy@posoco.in",
        "position": "GM",
        "cabinet number": 21,
        "skype": "hirak-roy21"
    }
]


def get_tag(prompt="поиска"):
    while True:
        tag = input(f"\tДля {prompt} по имени введите: n\n"
                    f"\tДля {prompt} по email введите: e\n"
                    f"\tДля {prompt} по skype введите: s\n"
                    ">>>>>>")
        if tag == "n" or tag == "e" or tag == "s":
            return tag
        else:
            print("\tНеразрешенное значение")


def input_ph_num(prompt="\tВведите номер телефона\n"
                        ">>>>>>"):
    while True:
        ph_num = input(prompt)
        match = re.search(r'\+?\d{3,11}', ph_num)
        if not (match is None):
            return match.group()
        else:
            print("Не удается распознать номер")


def input_email(prompt="\tВведите email\n"
                       ">>>>>>"):
    while True:
        email = input(prompt)
        if "@" in email:
            return email
        else:
            print("Не удается распознать email")


def input_cabinet_num(prompt="\tВведите номер кабинета\n"
                             ">>>>>>"):
    while True:
        try:
            cabinet_num = int(input(prompt))
            return cabinet_num
        except ValueError:
            print("Не удается распознать номер")


def exists_email(email):
    for employee in firm:
        for key, value in employee.items():
            if key == "email" and value == email:
                return True
    return False


def exists_skype(skype):
    for employee in firm:
        for key, value in employee.items():
            if key == "skype" and value == skype:
                return True
    return False


def find_by_key(key, value):
    for i in range(len(firm)):
        for k, v in firm[i].items():
            if k == key and v == value:
                return firm[i]
    return None


def get_coincidence_list_by_name(name_list):
    for n_i in range(len(name_list)):
        name_list[n_i] = name_list[n_i].lower()
    coincidence_list = [0 * i for i in range(len(firm))]
    was_find = False
    for i in range(len(firm)):
        for key, value in firm[i].items():
            if key == "full name":
                player_name = value.lower()
                for n in name_list:
                    if not (player_name.find(n) == -1):
                        was_find = True
                        coincidence_list[i] += 1
    return was_find, coincidence_list


def print_all():
    for employee in firm:
        for key, value in employee.items():
            print("\t{:>15}: {}".format(key, value))
        print()


def add_employee():
    full_name = input("\tВведите ФИО сотрудника\n"
                      ">>>>>>")
    ph_num = input_ph_num()
    while True:
        email = input_email()
        if not exists_email(email):
            break
        else:
            print("\tТакой email уже существует")
    position = input("\tВведите должность сотрудника\n"
                     ">>>>>>")
    cabinet_num = input_cabinet_num()
    while True:
        skype = input("\tВведите skype\n"
                      ">>>>>>")
        if not exists_skype(skype):
            break
        else:
            print("\tТакой skype уже существует")

    firm.append({"full name": full_name, "phone number": ph_num, "email": email,
                 "position": position, "cabinet number": cabinet_num, "skype": skype})


def delete_employee():
    tag = get_tag("удаления")
    if tag == "n":
        name = input("\tВведите имя сотрудника, которого хотите удалить\n"
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
                    remove = input(f"\tУдалить {firm[r_index]['full name']} ? (y/n)\n"
                                   ">>>>>>")
                    if remove == "y" or remove == "у":  # первый - "игрек", второй - "у"
                        firm.pop(r_index)
                        coincidence_list.pop(r_index)
                        print("\tСотрудник успешно удален")
                    else:
                        coincidence_list[r_index] = 0
                except ValueError:
                    break

    elif tag == "e":
        email = input_email("\tВведите email сотрудника, которого хотите удалить\n"
                            ">>>>>>")
        employee = find_by_key("email", email)
        if not (employee is None):
            firm.remove(employee)
            print("\tСотрудник успешно удален")
        else:
            print("\tСовпадений не найдено")
    elif tag == "s":
        skype = input("\tВведите skype сотрудника, которого хотите удалить\n"
                      ">>>>>>")
        employee = find_by_key("skype", skype)
        if not (employee is None):
            firm.remove(employee)
            print("\tСотрудник успешно удален")
        else:
            print("\tСовпадений не найдено")


def find_employee():
    tag = get_tag()
    if tag == "n":
        name = input("\tВведите имя сотрудника, которого хотите найти\n"
                     ">>>>>>")
        name_list = name.split()
        was_find, coincidence_list = get_coincidence_list_by_name(name_list)
        if not was_find:
            print("\tСовпадений не найдено")
        else:
            max_c = max(coincidence_list)
            while True:
                try:
                    f_index = coincidence_list.index(max_c)
                    print(firm[f_index])
                    coincidence_list[f_index] = 0
                except ValueError:
                    break

    elif tag == "e":
        email = input_email("\tВведите email сотрудника, которого хотите найти\n"
                            ">>>>>>")
        employee = find_by_key("email", email)
        if not (employee is None):
            print(employee)
        else:
            print("\tСовпадений не найдено")
    elif tag == "s":
        skype = input("\tВведите skype сотрудника, которого хотите найти\n"
                      ">>>>>>")
        employee = find_by_key("skype", skype)
        if not (employee is None):
            print(employee)
        else:
            print("\tСовпадений не найдено")


def changer(employee):
    while True:
        key = input(f"\tЧтобы изменить имя введите      : n\n"
                    f"\tЧтобы изменить телефон введите  : pn\n"
                    f"\tЧтобы изменить email введите    : e\n"
                    f"\tЧтобы изменить должность введите: p\n"
                    f"\tЧтобы изменить кабинет введите  : c\n"
                    f"\tЧтобы изменить skype введите    : s\n"
                    f"\tЧтобы завершить введите         : q\n"
                    ">>>>>>")
        if key == "q":
            break
        if key == "n":
            new_name = input("\tВведите новое имя сотрудника\n"
                             ">>>>>>")
            employee["full name"] = new_name
        elif key == "pn":
            new_ph_num = input_ph_num("\tВведите новый номер телефона\n"
                                      ">>>>>>")
            employee["phone number"] = new_ph_num
        elif key == "e":
            while True:
                new_email = input_email("\tВведите новый email\n"
                                        ">>>>>>")
                if not exists_email(new_email):
                    employee["email"] = new_email
                    break
                else:
                    print("\tТакой email уже существует")
        elif key == "p":
            new_position = input("\tВведите новую должность сотрудника\n"
                                 ">>>>>>")
            employee["position"] = new_position
        elif key == "c":
            new_c_num = input_cabinet_num("\tВведите новый номер кабинета\n"
                                          ">>>>>>")
            employee["cabinet number"] = new_c_num

        elif key == "s":
            while True:
                new_skype = input("\tВведите новый skype\n"
                                  ">>>>>>")
                if not exists_skype(new_skype):
                    employee["skype"] = new_skype
                    break
                else:
                    print("\tТакой skype уже существует")
        else:
            print("\tНеразрешенное значение")


def change_employee_data():
    tag = get_tag()
    if tag == "n":
        name = input("\tВведите имя сотрудника, данные которого хотите изменить\n"
                     ">>>>>>")
        name_list = name.split()
        was_find, coincidence_list = get_coincidence_list_by_name(name_list)
        if not was_find:
            print("\tСовпадений не найдено")
        else:
            max_c = max(coincidence_list)
            while True:
                try:
                    f_index = coincidence_list.index(max_c)
                    change = input(f"\tИзменить данные {firm[f_index]}? (y/n)\n"
                                   ">>>>>>")
                    if change == "y" or change == "у":  # первый - "игрек", второй - "у"
                        changer(firm[f_index])
                        print("\tДанные успешно изменены")
                    coincidence_list[f_index] = 0
                except ValueError:
                    break

    elif tag == "e":
        email = input_email("\tВведите email сотрудника, данные которого хотите изменить\n"
                            ">>>>>>")
        employee = find_by_key("email", email)
        if not (employee is None):
            changer(employee)
            print("\tДанные успешно изменены")
        else:
            print("\tСовпадений не найдено")
    elif tag == "s":
        skype = input("\tВведите skype сотрудника, данные которого хотите изменить\n"
                      ">>>>>>")
        employee = find_by_key("skype", skype)
        if not (employee is None):
            changer(employee)
            print("\tДанные успешно изменены")
        else:
            print("\tСовпадений не найдено")


commands_dict = {
    "print": print_all,
    "add": add_employee,
    "del": delete_employee,
    "find": find_employee,
    "change": change_employee_data

}

while True:
    command = input("\nВведите команду:\n"
                    "\tprint - вывод на экран всех данных\n"
                    "\tadd   - добавить нового сотрудника в список\n"
                    "\tdel   - удалить сотрудника\n"
                    "\tfind  - поиск сотрудника\n"
                    "\tchange- изменить данные сотрудника\n"
                    "\tquit  - завершение работы\n"
                    ">>>")
    if command == "quit":
        break
    try:
        commands_dict[command]()
    except KeyError:
        print("Команда не распознана")
