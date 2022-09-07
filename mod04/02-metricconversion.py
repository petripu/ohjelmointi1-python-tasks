# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.

print("Inches to centimeters converter, quit with negative number input")
inches = float(input("Input inches to be converted: "))

while inches > 0:
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters} centimeters")
    inches = float(input("Input inches to be converted: "))
