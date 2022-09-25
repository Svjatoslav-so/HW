import time
from threading import Thread

from Boat import Boat
from BoatsSiteProtocol import BoatsSiteProtocol
from Parser import Parser


class ParallelPageParser(Parser):

    def parse(self, site: BoatsSiteProtocol, res_list: list = None) -> list[Boat]:
        """
            This function returns a list of all the boats it was able to find on this site.

            If a res_list argument is passed, then the result will also be written to it (used for multithreading).
            This function for parsing the page itself allocates a separate thread.

            Args:
                site: This is the site to be parsed (must be BoatsSiteProtocol compliant).
                res_list: This is a list, if one was passed, then the result will be written to it.

            Returns:
                This function returns a list of objects of type Boat.
        """
        start = time.perf_counter()
        next_page = site.get_start_page()
        boats_on_pages = []
        threads = []
        while not (next_page is None):
            tree = self.get_tree(next_page)
            t = Thread(target=self._find_boats_on_page, args=(site, boats_on_pages, tree))
            t.start()
            threads.append(t)
            next_page = site.get_next_page_link(tree)
        for t in threads:
            t.join()
        end = time.perf_counter()
        print("PARALLEL_PAGE_PARSER: ", end - start)
        if not(res_list is None):
            res_list.extend(boats_on_pages)
        return boats_on_pages

    @staticmethod
    def _find_boats_on_page(site: BoatsSiteProtocol, page_boat_list: list, page_tree):
        """
            This function parses the html passed to it and adds the resulting objects to the passed list of objects.

            This is a helper function, it is needed to move this action to a separate thread.

        Args:
            site: This is an BoatsSiteProtocol object required for parsing html.
            page_boat_list: This is the list to which the result will be added.
            page_tree: This is a parsed page(HTML element tree).
        """
        page_boat_list.extend(site.find_boats(page_tree))
