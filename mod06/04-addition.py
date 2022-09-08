# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

def addition(arr):
    return sum(arr)


# if pre-determined numbers, use this to define array
# numbers = [3, 5, 7, 9]
numbers = input("insert array here: ")
arr = [int(x) for x in numbers.split()]
print(f"Sum of array is {addition(arr)}")
