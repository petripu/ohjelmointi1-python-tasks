# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

username = "python"
password = "rules"
counter = 5

username_input = input("Input username: ")
password_input = input("Input password: ")
while username_input != username or password_input != password:
    if counter == 1:
        print("Too many attempts!")
        break
    counter -= 1
    print(f"Login incorrect, try again. Attempts remaining {counter}")
    username_input = input("Input username: ")
    password_input = input("Input password: ")
else:
    print("Welcome!")
