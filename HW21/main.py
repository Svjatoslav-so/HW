import time
from threading import Thread

from BoatsParser import BoatsParser
from BoatsSite import BoatsSite
from FastParser import FastParser
from ParallelPageParser import ParallelPageParser

# boatshop24
boatshop24_url = "https://www.boatshop24.com"
# boatshop24_start_page = "https://www.boatshop24.com/boats-for-sale/class-sailing-boats/page-40/"
boatshop24_start_page = "https://www.boatshop24.com/boats-for-sale/class-sailing-boats/"
boatshop24_li_list = '//*[@id="right-content"]/div[2]/ol/li[@data-listing-id]'
boatshop24_next_page = "//ul[@class='pagination']/li/a[@class='next']/@href"
boatshop24_name = 'div/div[2]/div[1]/div[1]/h2/text()'
boatshop24_link = 'div/div[2]/div[1]/div[@class = "name"]/a/@href'
boatshop24_price = 'div/div[2]/div[1]/div[@class = "price"]/text()'
boatshop24_location = 'div/div[2]/div[1]/div[@class = "location"]/text()'

boatshop24 = BoatsSite(boatshop24_url, boatshop24_start_page, boatshop24_li_list, boatshop24_name,
                       boatshop24_link, boatshop24_price, boatshop24_location, boatshop24_next_page)

# boat24
boat24_url = "https://www.boat24.com/en/"
boat24_start_page = "https://www.boat24.com/en/sailboats/"
boat24_li_list = '//*[@id="sticky-header-trigger"]/div/ul/li/div[@data-link]'
boat24_next_page = "//div[@class='pagination l-mt-64 l-mb-64']/" \
                   "span[contains(text(),'Next page')]/@data-link"
boat24_name = 'div[@class="blurb__main"]/h3[@class="blurb__title"]/a/text()'
boat24_link = 'div[@class="blurb__main"]/h3[@class="blurb__title"]/a/@href'
boat24_price = 'aside[@class="blurb__side"]/p[@class="blurb__price"]/text()'
boat24_location = 'div[@class="blurb__main"]/p[@class="blurb__location"]/text()'

boat24 = BoatsSite(boat24_url, boat24_start_page, boat24_li_list, boat24_name, boat24_link,
                   boat24_price, boat24_location, boat24_next_page)

# yachtworld
yachtworld_url = "https://www.yachtworld.com/"
yachtworld_start_page = "https://www.yachtworld.com/boats-for-sale/type-sail/"
yachtworld_li_list = '//div[@class="listings-container"]/a'
# yachtworld_next_page = "//div[@class='search-page-nav']/a[@class='icon-chevron-right ']/@href"
yachtworld_next_page = "//div[@class='search-page-nav']/a[@class='active']//following-sibling::a[2]/@href"
yachtworld_name = 'div[contains(@class,"row listing-card")]/div[@class="listing-card-information"]/h2/text()'
yachtworld_link = '@href'
yachtworld_price = 'div[contains(@class,"row listing-card")]/div[@class="listing-card-information"]/' \
                   'div[@class="price"]//text()'
yachtworld_location = 'div[contains(@class,"row listing-card")]/div[@class="listing-card-information"]/' \
                      'div[@class="listing-card-location"]/text()'
yachtworld = BoatsSite(yachtworld_url, yachtworld_start_page, yachtworld_li_list, yachtworld_name,
                       yachtworld_link, yachtworld_price, yachtworld_location, yachtworld_next_page,
                       lambda index: "?page=" + str(index) if index > 0 else '')


parallel_parser = ParallelPageParser()
recurs_parser = BoatsParser()
new_parser = FastParser(10)

boats_list = []

t1 = Thread(target=parallel_parser.parse, args=(boatshop24, boats_list))
t2 = Thread(target=recurs_parser.parse, args=(boat24, boats_list))
t2p = Thread(target=parallel_parser.parse, args=(boat24, boats_list))
t3 = Thread(target=new_parser.parse, args=(yachtworld, boats_list))
thread = [t1, t2, t3]
# thread = [t2, t2p]
start_time = time.perf_counter()
for t in thread:
    t.start()
for t in thread:
    t.join()
end_time = time.perf_counter()
print("ALL_TIME: ", end_time - start_time)
print("ALL_BOATS_COUNT: ", len(boats_list))

