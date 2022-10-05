import functools
import sqlite3
from sqlite3 import Cursor


class BoatDB:
    _boats_table = "boats"  # название таблицы для хранения лодок
    _users_table = "users"  # название таблицы для хранения пользователей
    _filters_table = "filters"  # название таблицы для хранения фильтров пользователя
    _db_name: str  # название базы данных

    def __init__(self, db_name):
        self.set_db_name(db_name)

    def set_db_name(self, db_name: str):
        if db_name.endswith(".db"):
            self._db_name = db_name
        else:
            self._db_name = db_name + ".db"

    def create_boats_table(self, cur: Cursor):
        """Данная функция создает в базе данных таблицу для хранения лодок."""
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {self._boats_table}(
                        title TEXT NOT NULL,
                        price REAL,
                        link TEXT PRIMARY KEY NOT NULL,
                        location TEXT,
                        year INTEGER,
                        length REAL,
                        beam REAL,
                        draught REAL,
                        hull_material TEXT,
                        fuel_type TEXT,
                        other_param TEXT,
                        description TEXT,
                        photo INTEGER,
                        category TEXT,
                        type TEXT
                        )""")

    def create_users_table(self, cur: Cursor):
        """Данная функция создает в базе данных таблицу для хранения пользователей. """
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {self._users_table}(
                        id INTEGER PRIMARY KEY NOT NULL,
                        first_name TEXT,
                        last_name TEXT
                        );""")

    def create_filters_table(self, cur: Cursor):
        """Данная функция создает в базе данных таблицу для хранения пользовательских фильтров. """
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {self._filters_table}(
                        user_id INTEGER PRIMARY KEY NOT NULL,
                        boat_name TEXT,
                        min_price REAL,
                        max_price REAL,
                        location TEXT,
                        min_year INTEGER,
                        max_year INTEGER,
                        min_length REAL,
                        max_length REAL,
                        min_draught REAL,
                        max_draught REAL,
                        hull_material TEXT,
                        fuel_type TEXT,
                        category TEXT,
                        type TEXT,
                        FOREIGN KEY(user_id) REFERENCES {self._users_table} (id) ON DELETE CASCADE
                        );""")

    def create_db(self):
        """Данная функция создает базу данных и таблицы в ней. """
        con = sqlite3.connect(self._db_name)
        cur = con.cursor()
        self.create_boats_table(cur)
        self.create_users_table(cur)
        self.create_filters_table(cur)
        con.close()

    def add_boats(self, boats: list[tuple]):
        """
        Данная функция добавляет лодки в таблицу лодок в базе данных.

        Args:
            boats: список кортежей(каждый кортеж описывает лодку).
                   Размерность кортежа должна совпадать с количеством столбцов в таблице лодок в базе данных.
                   Если какой-либо параметр для лодки не указан, то необходимо указать None.
        """
        con = sqlite3.connect(self._db_name)
        cur = con.cursor()
        placeholders = "?, " * (len(boats[0]) - 1) + "?"
        cur.executemany(f"""REPLACE INTO {self._boats_table} VALUES({placeholders})""", boats)
        con.commit()
        con.close()

    def add_user(self, user: tuple):
        """
        Данная функция добавляет пользователя в таблицу пользователей в базе данных.

        Args:
            user: кортеж описывающий пользователя. Размерность кортежа должна совпадать с количеством столбцов
                  в таблице пользователей в базе данных. Если какой-либо параметр для пользователя не указан,
                  то необходимо указать None.
        """
        con = sqlite3.connect(self._db_name)
        cur = con.cursor()
        placeholders = "?, " * (len(user) - 1) + "?"
        cur.execute(f"""REPLACE INTO {self._users_table} VALUES({placeholders})""", user)
        con.commit()
        con.close()

    def add_filter(self, boat_filter: dict):
        """
        Данная функция добавляет фильтр в таблицу пользовательских фильтров в базе данных.

        Args:
            boat_filter: словарь описывающий фильтр(ключи для словаря берутся из множества названий столбцов таблицы
                         фильтра в базе данных). В словаре указываются только те параметры
                         для которых установлены значения.
        """
        keys = list(boat_filter.keys())
        values = list(boat_filter.values())

        con = sqlite3.connect(self._db_name)
        cur = con.cursor()
        cur.execute(f"""REPLACE INTO {self._filters_table} 
                        ({functools.reduce(lambda x, y: x + y + ", ", keys, "")[:-2]})
                        VALUES({functools.reduce(lambda x, y: x + '"' + str(y) + '"' + ', ', values, "")[:-2]})""")
        con.commit()
        con.close()

    def get_user(self, user_id: int, columns: str = "*") -> tuple | None:
        """
        Данная функция ищет пользователя по id в таблице позьзователей в базе данных.

        Args:
            user_id: id позьзователя которого мы ищем.
            columns: строка содержащая названия столбцов таблицы пользователей, значения которых мы хотим получить.
                     По умолчанию "*" - все столбцы.
        Returns:
            Функция возвращает кортеж со значениями столбцов указанных в columns.
        """
        try:
            con = sqlite3.connect(self._db_name)
            cur = con.cursor()
            res = cur.execute(f"""SELECT {columns} FROM {self._users_table} WHERE id = {str(user_id)}""")
            user = res.fetchone()
            con.close()
            return user
        except sqlite3.OperationalError as e:
            print(f"Error in function {self.get_user} ->", e)

    def get_filter(self, user_id: int, columns: str = "*") -> tuple | None:
        """
        Данная функция ищет фильтр по id в таблице фильтров в базе данных.

        Args:
            user_id: id позьзователя фильтр которого мы ищем.
            columns: строка содержащая названия столбцов таблицы фильтров, значения которых мы хотим получить.
                     По умолчанию "*" - все столбцы.
        Returns:
            Функция возвращает кортеж со значениями столбцов указанных в columns.
        """
        try:
            con = sqlite3.connect(self._db_name)
            cur = con.cursor()
            res = cur.execute(f"""SELECT {columns} FROM {self._filters_table} WHERE user_id = {str(user_id)}""")
            u_filter = res.fetchone()
            con.close()
            return u_filter
        except sqlite3.OperationalError as e:
            print(f"Error in function {self.get_filter} ->", e)

    @staticmethod
    def __text_filter(boat_filter: dict, filter_name: str, param_name: str) -> str | None:
        """
        Вспомогательная функция, используется для добавления фильтрации текстовых полей таблицы лодок в SQL-запросы.

        Args:
            boat_filter: словарь, описывающий применяемый фильтр.
            filter_name: название параметра фильтра, который мы хотим преобразовать в SQL-фильтр.
                         Название должно быть из множества названий столбцов в таблице фильтра в базе данных.
            param_name:  название параметра лодки на который наклабывается фильтр. Название должно быть из множества
                         названий столбцов в таблице лодок в базе данных.

        Returns:
            Функция возвращает строку(часть SQL-запроса, отвечающую за фильтрацию иказанного параметра), если фильтр на
            указанный параметр есть в словаре boat_filter. Если его нет, тогда пустую строку.
        """
        if filter_name in boat_filter.keys():
            return f"{param_name} LIKE '%{boat_filter[filter_name]}%' AND "
        return ""

    @staticmethod
    def __range_filter(boat_filter: dict, from_filter_name: str, to_filter_name: str, param_name: str):
        """
        Вспомогательная функция, добавляет диапазон фильтрации для числовых полей в таблице лодок в SQL-запросы.

        Args:
            boat_filter:      словарь, описывающий применяемый фильтр.
            from_filter_name: название параметра фильтра, который указывает начало диапазона для указанного параметра
                              лодки. Название должно быть из множества названий столбцов в таблице фильтра.
            to_filter_name:   название параметра фильтра, который указывает конец диапазона для указанного параметра
                              лодки. Название должно быть из множества названий столбцов в таблице фильтра.
            param_name:       название параметра лодки на который наклабывается фильтр. Название должно быть из
                              множества названий столбцов в таблице лодок в базе данных.

        Returns:
            Функция возвращает строку(часть SQL-запроса, отвечающую за фильтрацию иказанного параметра), если фильтр на
            указанный параметр есть в словаре boat_filter. Если его нет, тогда пустую строку.
        """
        keys = boat_filter.keys()
        if from_filter_name in keys and to_filter_name in keys:
            return f"{param_name} BETWEEN {boat_filter[from_filter_name]} AND {boat_filter[to_filter_name]} AND "
        if from_filter_name in keys:
            return f"{param_name} >= {boat_filter[from_filter_name]} AND "
        if to_filter_name in keys:
            return f"{param_name} <= {boat_filter[to_filter_name]} AND "
        return ""

    def get_boats(self, boat_filter: dict, columns: str = "*") -> list[tuple]:
        """
        Данная функция ищет лодки удовлетворяющие фильтру в таблице лодок.

        Args:
            boat_filter: словарь, описывающий применяемый фильтр.
            columns: строка содержащая названия столбцов таблицы лодок, значения которых мы хотим получить.
                     По умолчанию "*" - все столбцы.
        Returns:
            Функция возвращает список кортежей со значениями столбцов из таблицы лобок указанных в columns.
        """
        con = sqlite3.connect(self._db_name)
        cur = con.cursor()
        request = f"SELECT {columns} FROM {self._boats_table}"
        if len(boat_filter) > 0:
            request += " WHERE "

            request += self.__text_filter(boat_filter, "boat_name", "title")
            request += self.__text_filter(boat_filter, "location", "location")
            request += self.__text_filter(boat_filter, "hull_material", "hull_material")
            request += self.__text_filter(boat_filter, "fuel_type", "fuel_type")
            request += self.__text_filter(boat_filter, "category", "category")
            request += self.__text_filter(boat_filter, "type", "type")
            request += self.__range_filter(boat_filter, "min_price", "max_price", "price")
            request += self.__range_filter(boat_filter, "min_year", "max_year", "year")
            request += self.__range_filter(boat_filter, "min_length", "max_length", "length")
            request += self.__range_filter(boat_filter, "min_draught", "max_draught", "draught")

            request = request[:-4]

        print(request)
        res = cur.execute(request)
        boats = res.fetchall()
        con.close()
        return boats
