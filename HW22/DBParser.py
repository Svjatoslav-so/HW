import sqlite3

from BoatsSiteProtocol import BoatsSiteProtocol
from Parser import Parser


class DBParser(Parser):

    def parse_to_db(self, site: BoatsSiteProtocol, db: str):
        """
            This function parses the site and saves the received data to the database

            Args:
                site: This is the site to be parsed (must be BoatsSiteProtocol compliant).
                db: This is the database to which the data will be saved.
        """
        # start = time.perf_counter()

        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute("""CREATE TABLE  IF NOT EXISTS Boats (
                    title TEXT ,
                    price TEXT, 
                    link TEXT PRIMARY KEY, 
                    location TEXT
                    );""")

        next_page = site.get_start_page()
        while not (next_page is None):
            tree = self.get_tree(next_page)
            page_boats_list = site.find_boats(tree)
            cur.executemany("""REPLACE INTO Boats VALUES(?, ?, ?, ?)""",
                            [boat.to_db() for boat in page_boats_list])
            next_page = site.get_next_page_link(tree)

        con.commit()
        con.close()
        # end = time.perf_counter()
        # print("PARALLEL_PAGE_PARSER: ", end - start)

