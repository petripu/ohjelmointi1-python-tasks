# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin
# Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

goal = random.randint(1,10)
user_input = -1
while user_input != goal:
    user_input = int(input("Guess the number between 1 and 10: "))
    if user_input < goal:
        print("Your guess was too small!!!")
    elif user_input > goal:
        print("Your guess was too big!!!")
    else:
        print(f"Correct!! Answer was {goal}")
