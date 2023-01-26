# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan
# nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä
# esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen
# nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random


# throw gets value from input
def throw(sides):
    return random.randint(1, sides)


# user can input any number of sides for the dice
sides = int(input("Whats the number of sides on the dice?: "))
print(f"Throwing the dice until {sides}!")
dice = 0
throws = 0
while dice != sides:
    dice = throw(sides)
    print(dice)
    throws += 1
else:
    print(f"It took {throws} throws until success!")
