# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

airports = {"EFHK":"Helsinki-Vantaa Airport",
            "WSSS":"Singapore Changi Airport"}
choice = 0
while choice != 3:
    choice = int(input("Choose 1 for adding a new airport information, "
                       "2 for searching airports or 3 for exiting the program\n"))
    if choice == 1:
        code = input("Input airport ICAO code: ").upper()
        airports[code] = input("Name of the airport: ")
    elif choice == 2:
        code = input("Input airport ICAO code: ").upper()
        if code in airports:
            print(f"{code} matches the airport {airports[code]}")
        else:
            print("Airport matching that code not found :o")

print("Thanks for using Airport DataBas€ 666 xoxo!!")
