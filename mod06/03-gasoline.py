# Kirjoita funktio, joka saa parametrinaan bensiinin määrän
# Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.

liter_multiplier = 3.78541


def conversion(gallons):
    return gallons * liter_multiplier


gallons = 1
while gallons >= 0:
    gallons = float(input("Gasoline amount in gallons: "))
    if gallons < 0:
        break
    result = conversion(gallons)
    print(f"Gasoline amount in liters is {round(result, 2)} ")
