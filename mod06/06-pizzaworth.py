# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math


# pizza value function
def pizza_area(diameter, price):
    radius = (diameter / 2) / 100  # get radius and convert cm to m
    area = math.pi * (radius ** 2)  # calculate area using **2
    value = price / area  # for clarity
    return value


# ask for pizza data
pizza1_diameter = float(input("Pizza 1 diameter in cm: "))
pizza1_price = float(input("Pizza 1 price in euro: "))
pizza2_diameter = float(input("Pizza 2 diameter in cm: "))
pizza2_price = float(input("Pizza 2 price in euro: "))

pizza1 = pizza_area(pizza1_diameter, pizza1_price)
pizza2 = pizza_area(pizza2_diameter, pizza2_price)

if pizza1 < pizza2:
    print("Pizza 1 has better value.")
elif pizza1 == pizza2:
    print("Both pizzas are equally amazing!!")
else:
    print("Pizza 2 has better value.")

# print(pizza1, pizza2) # to see values
