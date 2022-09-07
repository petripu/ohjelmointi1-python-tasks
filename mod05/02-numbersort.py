# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä
# suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää
# antamalla sort-metodille argumentiksi reverse=True.

# setup array and ask for first input
numbers = []
number = input("Input first number: ")

# loop for adding numbers to array
while -1:
    if number == "":
        break
    else:
        numbers.append(int(number))
    number = input("Input next number: ")

# sort numbers and print top 5
numbers.sort(reverse=True)
print(f"Largest five numbers are: {str(numbers[:5])[1:-1]}")
