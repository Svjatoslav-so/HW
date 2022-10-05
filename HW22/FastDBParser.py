import sqlite3
from threading import Thread

from BoatsSiteProtocol import BoatsSiteProtocol
from Parser import Parser


class FastDBParser(Parser):
    __threads_num: int  # number of threads used for parsing

    def __init__(self, threads_num: int = 5):
        self.set_threads_num(threads_num)

    def set_threads_num(self, threads_num: int):
        if (type(threads_num) == int) and (threads_num > 0):
            self.__threads_num = threads_num
        else:
            self.__threads_num = 5

    def parse_to_db(self, site: BoatsSiteProtocol, db: str):
        """
           This function parses the site in several threads and stores the data in the database

            Args:
                site: This is the site to be parsed (must be BoatsSiteProtocol compliant).
                db: This is the database to which the data will be saved.
        """
        # start = time.perf_counter()
        threads = []
        for i in range(1, self.__threads_num+1):
            print(f"I {i}")
            p_t = Thread(target=self._parse_by_step, args=(site, db, i, self.__threads_num))
            threads.append(p_t)
            p_t.start()
        for p_t in threads:
            p_t.join()
        # end = time.perf_counter()
        # print("PARSE: ", end - start)

    def _parse_by_step(self, site: BoatsSiteProtocol, db: str, start: int, step: int):
        """
            This is a helper function, it parses the pages of the site with the specified step.

            The result of parsing is added to the database db.
            This function for parsing the page itself allocates a separate thread.

            Args:
                site: This is the site to be parsed (must be BoatsSiteProtocol compliant).
                db: This is the database to which the data will be saved.
                start: This is the index of the page to start parsing from.
                step: This is the step with which the function will iterate through the pages of the site
                      starting from start.
        """
        boats_list = []
        find_threads = []
        page_index = start
        while True:
            next_page = site.get_next_page_link(index=page_index)
            # print(f"T: {start} NEXT: {next_page}")
            tree = self.get_tree(next_page)
            if not (tree is None):
                t = Thread(target=self._find_boats_on_page, args=(site, boats_list, tree))
                t.start()
                find_threads.append(t)
                page_index += step
            else:
                break
        for t in find_threads:
            t.join()

        con = sqlite3.connect(db)
        con.execute("""CREATE TABLE  IF NOT EXISTS Boats (
                    title TEXT ,
                    price TEXT, 
                    link TEXT PRIMARY KEY, 
                    location TEXT
                    );""")
        try:
            with con:
                con.executemany("""REPLACE INTO Boats VALUES(?, ?, ?, ?)""",
                                [boat.to_db() for boat in boats_list])
        except Exception as e:
            print(e)
        finally:
            con.close()

    @staticmethod
    def _find_boats_on_page(site, boat_list, page_tree):
        """
            This function parses the html passed to it and adds the resulting objects to the passed list of objects.

            This is a helper function, it is needed to move this action to a separate thread.

        Args:
            site: This is an BoatsSiteProtocol object required for parsing html.
            boat_list: This is the list to which the result will be added.
            page_tree: This is a parsed page(HTML element tree).
        """
        boat_list.extend(site.find_boats(page_tree))
