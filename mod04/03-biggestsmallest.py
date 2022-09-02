# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

user_input = input("Input number: ")
max_value = min_value = int(user_input)

while user_input != "":
    user_input = input("Input number: ")
    if user_input == "":
        break
    user_input_int = int(user_input)
    if user_input_int < min_value:
        min_value = user_input_int
    if user_input_int > max_value:
        max_value = user_input_int
print(f"Smallest number is {min_value} and biggest number is {max_value}.")
