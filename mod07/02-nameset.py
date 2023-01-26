# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen
# ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet
# yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

# setting up set and variable for input
names = set()
name = "funny name hehe :3"
# start loop for input
while name != "":
    name = input("Input name to be added: ")
    if not name:
        continue  # this avoids going back to else statement when user exits
    elif name not in names:
        names.add(name)
        print("New name added.")
    else:
        print("Name already in list")

print("Names in the list are:")
for f in names:
    print(f)
