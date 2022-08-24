# Task 2
ef_dictionary = {
    "papillon": "butterfly",
    "hirondelle": "swallow",
    "pamplemousse": "grapefruit",
    "parapluie": "umbrella",
    "chaleur": "heat",
    "nuage": "cloud",
    "soleil": "Sun",
    "tournesol": "sunflower",
    "etoile": "star",
    "floraison": "bloom",
    "coquillage": "shellfish",
    "formidable": "tremendous",
    "plaisir": "pleasure",
    "citronnade": "lemonade ",
    "myrtille": "blueberry"
}


def print_all():
    for key, value in ef_dictionary.items():
        print("\t{:<20} {}".format(key, value))
    print()


def add_word():
    word = input("\tВведите слово(на французском)\n"
                 ">>>>>>")
    word = word.lower()
    translation = input("\tВведите перевод(на английском)\n"
                        ">>>>>>")
    ef_dictionary[word] = translation


def delete_word():
    word = input("\tВведите слово, которое хотите удалить(на французском)\n"
                 ">>>>>>")
    was_deleted = ef_dictionary.pop(word, False)
    if not was_deleted:
        print("\tСлово не найдено")
    else:
        print("\tСлово успешно удалено")


def find_word():
    word = input("\tВведите слово, которое хотите найти(на французском)\n"
                 ">>>>>>")
    word = word.lower()
    translation = ef_dictionary.get(word)
    if translation is None:
        print("\tСлово не найдено")
    else:
        print("\t{:<20} {}".format(word, translation))


def change_word_translation():
    word = input("\tВведите слово, которое хотите изменить(на французском)\n"
                 ">>>>>>")
    if word in ef_dictionary.keys():
        translation = input("\tВведите новый перевод(на английском)\n"
                            ">>>>>>")
        ef_dictionary[word] = translation
    else:
        print("\tСлово не найдено")


commands_dict = {
    "print": print_all,
    "add": add_word,
    "del": delete_word,
    "find": find_word,
    "change": change_word_translation

}

while True:
    command = input("\nВведите команду:\n"
                    "\tprint - вывод на экран всех слов в словаре\n"
                    "\tadd   - добавить новое слово в словарь\n"
                    "\tdel   - удалить слово\n"
                    "\tfind  - найти слово\n"
                    "\tchange- изменить перевод слова\n"
                    "\tquit  - завершение работы\n"
                    ">>>")
    if command == "quit":
        break
    try:
        commands_dict[command]()
    except KeyError:
        print("Команда не распознана")
