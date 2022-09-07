# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja
# ilmoittaa, onko se alkuluku. Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla
# 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan
# jakaa tasan myös luvulla 3 tai luvulla 7.

# set a flag to avoid multiple prints
flag = 0
number = int(input("Input number: "))

# check number using loop
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            flag = 1
            break
else:
    flag = 1

# print according to flag
if flag == 1:
    print(f"{number} is not prime number.")
else:
    print(f"{number} is a prime number.")
