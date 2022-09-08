# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
# nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa
# niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random


# define function for dice throw
def throw():
    return random.randint(1, 6)


# throw the dice until desired result
print("Throwing the dice untill 6!")
dice = 0
while dice != 6:
    dice = throw()
    print(dice)
