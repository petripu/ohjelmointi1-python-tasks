# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
# parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
# ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def print_even(arr):
    even_numbers = []
    for number in arr:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


# if pre-determined numbers, use this to define array
# numbers = [3, 4, 5, 7, 8, 9]
numbers = input("insert array here: ")
arr = [int(x) for x in numbers.split()]
print(f"Numbers given are:  {str(arr)[1:-1]}")
print(f"Even numbers are:   {str(print_even(arr))[1:-1]}")
