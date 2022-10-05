from DBManager import BoatDB

db = BoatDB("TPBoat")
db.create_db()
db.add_boats([("X-Yachts X4.3", 250200,
               "https://www.boat24.com/en/https://www.boat24.com/en/sailboats/najad/najad-331/detail/5794217/",
               "Italy", 2016, 38, 3, 200, "Fiberglass", "Gas", None, "GOOD BOAT", "398778893", "sailing", "monohull"),
              ("Jeanneau Sun Odyssey 30 i", 628000,
               "https://www.boat24.com/en/https://www.boat24.com/en/sailboats/najad/najad-331/detail/9673717/",
               "Italy", 2015, 40, 3.8, 90, "Fiberglass", "Electric",
               None, "GOOD BOAT", "39883893", "sailing", "catamaran"),
              ("Jeanneau Sun Fast 3200", 290000,
               "https://www.boat24.com/en/https://www.boat24.com/en/sailboats/najad/najad-331/detail/3820617/",
               "Italy", 2020, 45, 4, 90, "Fiberglass", "Diesel", None, "GOOD BOAT", "39803893", "motosail",
               "catamaran"),
              ("X-Yachts X-302", 29000,
               "https://www.boat24.com/en/https://www.boat24.com/en/sailboats/najad/najad-331/detail/5170217/",
               "Italy", 1986, 25, 2.4, 150, "Wood", "Electric", None, "Fair BOAT", 398433893, "sailing", "monohull")
              ])
db.add_user((34, "Vova", "Dudin"))
db.add_filter({"user_id": 34,
               "boat_name": "X-Yachts",
               "min_price": 0,
               "max_price": 200000,
               "min_year": 2010,
               "min_length": 30,
               "category": "sailing"})

print(db.get_user(314, "id"))
print(db.get_user(34))
print(db.get_filter(314))
print(db.get_filter(34))
print(db.get_boats({
    # "boat_name": "38",
    # "max_price": 100000,
    # "min_price": 20000,
    "location": "italy",
    "min_year": 1990,
    "max_year": 2010,
    "min_length": 20,
    "max_length": 40,
    "min_draught": 50,
    "max_draught": 200,
    # "hull_material": "wood",
    "fuel_type": "diesel",
    "category": "sail",
    "type": "monohull",
}))
