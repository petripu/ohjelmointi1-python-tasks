# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

dices = int(input("How many dices to throw?: "))
total = 0
# loops from 0 to dices -1
for i in range(dices):
    dice = random.randint(1,6)
    total += dice

print(f"Sum of {dices} dices you throw is {total}")
