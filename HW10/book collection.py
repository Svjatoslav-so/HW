# Task 4

books = [
    {
        "author": "Дэвид Томас, Эндрю Хант",
        "title": "Программист-прагматик. Ваш путь к мастерству» (2-е, юбилейное издание к 20-летию выхода книги)",
        "genre": "Программирование",
        "year": 2020,
        "number of pages": 368,
        "publishing house": "Вильямс",
    },
    {
        "author": "Роберт Мартин",
        "title": "Чистый код: создание, анализ и рефакторинг",
        "genre": "Программирование",
        "year": 2021,
        "number of pages": 464,
        "publishing house": "Питер",
    },
    {
        "author": "Стив Макконнелл",
        "title": "Совершенный код. Мастер-класс",
        "genre": "Программирование",
        "year": 2017,
        "number of pages": 896,
        "publishing house": "БХВ",
    },
    {
        "author": "Дональд Кнут",
        "title": "Искусство программирования. Том 1",
        "genre": "Программирование",
        "year": 2020,
        "number of pages": 720,
        "publishing house": "Вильямс",
    }
]


def get_tag(prompt="поиска"):
    while True:
        tag = input(f"\tДля {prompt} по названию введите: t\n"
                    f"\tДля {prompt} по жанру введите   : g\n"
                    f"\tДля {prompt} по автору введите  : a\n"
                    f"\tДля {prompt} по году введите    : y\n"
                    f"\tДля {prompt} по изданию введите : p\n"
                    ">>>>>>")
        if tag == "t" or tag == "g" or tag == "a" or tag == "y" or tag == "p":
            return tag
        else:
            print("\tНеразрешенное значение")


def print_all():
    for book in books:
        for key, value in book.items():
            print(f"\t{key}: {value}")
        print()


def add_book():
    title = input("\tВведите название книги\n"
                  ">>>>>>")
    author = input("\tВведите автора книги\n"
                   ">>>>>>")
    genre = input("\tВведите жанр книги\n"
                  ">>>>>>")
    pub_house = input("\tВведите издательство\n"
                      ">>>>>>")
    while True:
        try:
            year = int(input("\tВведите год издания книги\n"
                             ">>>>>>"))
            break
        except ValueError:
            print("\tНекорректные данные\n")
    while True:
        try:
            pages_num = int(input("\tВведите количество страниц книги\n"
                                  ">>>>>>"))
            if pages_num <= 0:
                raise ValueError
            break
        except ValueError:
            print("\tНекорректные данные\n")

    books.append({"author": author, "title": title, "genre": genre, "year": year,
                  "number of pages": pages_num, "publishing house": pub_house})


def delete_book():
    title = input("\tВведите название книги, которую хотите удалить\n"
                  ">>>>>>")
    title = title.split()
    was_find, coincidence_list = get_coincidence_list_by_key("title", title)
    if not was_find:
        print("\tСовпадений не найдено")
    else:
        max_c = max(coincidence_list)
        while True:
            try:
                r_index = coincidence_list.index(max_c)
                remove = input(f"\tУдалить \"{books[r_index]['title']}\" ? (y/n)\n"
                               ">>>>>>")
                if remove == "y" or remove == "у":  # первый - "игрек", второй - "у"
                    books.pop(r_index)
                    coincidence_list.pop(r_index)
                    print("\tКнига успешно удалена")
                else:
                    coincidence_list[r_index] = 0
            except ValueError:
                break


def get_coincidence_list_by_key(key, value_list):
    if type(value_list) is list:
        for n_i in range(len(value_list)):
            value_list[n_i] = value_list[n_i].lower()
    coincidence_list = [0 * i for i in range(len(books))]
    was_find = False
    for i in range(len(books)):
        for k, v in books[i].items():
            if k == key:
                if type(v) is str:
                    value = v.lower()
                else:
                    value = v
                if type(value_list) is list:
                    for n in value_list:
                        if not (value.find(n) == -1):
                            was_find = True
                            coincidence_list[i] += 1
                else:
                    if value == value_list:
                        was_find = True
                        coincidence_list[i] += 1
    return was_find, coincidence_list


def find_book():
    tag = get_tag()
    key = {
        "t": "title",
        "g": "genre",
        "a": "author",
        "y": "year",
        "p": "publishing house"
    }
    f_value = input("\tВведите данные для поиска\n"
                    ">>>>>>")
    try:
        f_value = int(f_value)
    except ValueError:
        f_value = f_value  # заглушка
    if isinstance(f_value, str):
        f_value = f_value.split()
    was_find, coincidence_list = get_coincidence_list_by_key(key[tag], f_value)
    if not was_find:
        print("\tСовпадений не найдено")
    else:
        max_c = max(coincidence_list)
        while True:
            try:
                f_index = coincidence_list.index(max_c)
                print(books[f_index])
                coincidence_list[f_index] = 0
            except ValueError:
                break


def changer(book):
    while True:
        tag = input(f"\tЧтобы изменить назване введите           : t\n"
                    f"\tЧтобы изменить жанр введите              : g\n"
                    f"\tЧтобы изменить автора введите            : a\n"
                    f"\tЧтобы изменить год введите               : y\n"
                    f"\tЧтобы изменить количество страниц введите: pag\n"
                    f"\tЧтобы изменить издательство введите      : pub\n"
                    f"\tЧтобы завершить введите                  : q\n"
                    ">>>>>>")
        key = {
            "t": "title",
            "g": "genre",
            "a": "author",
            "pub": "publishing house"
        }
        if tag == "q":
            break
        if tag == "t" or tag == "g" or tag == "a" or tag == "pub":
            value = input("\tВведите новое значение\n"
                          ">>>>>>")
            book[key[tag]] = value
        elif tag == "pag":
            while True:
                try:
                    new_pages_num = int(input("\tВведите новое количество страниц книги\n"
                                              ">>>>>>"))
                    if new_pages_num <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("\tНекорректные данные\n")
            book["number of pages"] = new_pages_num
        elif tag == "y":
            while True:
                try:
                    new_year = int(input("\tВведите новый год издания книги\n"
                                         ">>>>>>"))
                    break
                except ValueError:
                    print("\tНекорректные данные\n")
            book["year"] = new_year


def change_book_data():
    title = input("\tВведите название книги, данные которой вы хотите изменить\n"
                  ">>>>>>")
    title = title.split()
    was_find, coincidence_list = get_coincidence_list_by_key("title", title)
    if not was_find:
        print("\tСовпадений не найдено")
    else:
        max_c = max(coincidence_list)
        while True:
            try:
                f_index = coincidence_list.index(max_c)
                change = input(f"\tИзменить данные \"{books[f_index]}\"? (y/n)\n"
                               ">>>>>>")
                if change == "y" or change == "у":  # первый - "игрек", второй - "у"
                    changer(books[f_index])
                    print("\tДанные успешно изменены")
                coincidence_list[f_index] = 0
            except ValueError:
                break


commands_dict = {
    "print": print_all,
    "add": add_book,
    "del": delete_book,
    "find": find_book,
    "change": change_book_data

}
mama = "2020"
mama.lower()
while True:
    command = input("\nВведите команду:\n"
                    "\tprint - вывод на экран всех книг\n"
                    "\tadd   - добавить новую книгу в список\n"
                    "\tdel   - удалить книгу\n"
                    "\tfind  - поиск книги\n"
                    "\tchange- изменить данные о книге\n"
                    "\tquit  - завершение работы\n"
                    ">>>")
    if command == "quit":
        break
    try:
        commands_dict[command]()
    except KeyError:
        print("Команда не распознана")
