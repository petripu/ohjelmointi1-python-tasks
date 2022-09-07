# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta
# niiden läpikäymiseen.

# ask user for city names
cities = []
for i in range(5):
    city = input("Input name of the city: ")
    cities.append(city)

# print cities in order
for city in cities:
    print(city)

# make a numbered list using this
# for i, city in enumerate(cities):
#    print(i, city)
