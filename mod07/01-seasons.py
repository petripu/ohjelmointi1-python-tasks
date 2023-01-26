# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä
# vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia
# vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

def ordinal(n): # needed to format output nicely in english
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, "th")


seasons = ("winter", "winter", "spring",
           "spring", "spring", "summer",
           "summer", "summer", "fall",
           "fall", "fall", "winter")
month = int(input("Number of month: "))
season = seasons[month - 1]
ordinal_month = ordinal(month)
print(f"The {ordinal_month} month is in {season}")

# this solution is kinda disgusting but had a good laugh making it

# another solution my friend came up with and i want to save it cause its so good
# seasons = ["winter", "spring", "summer", "fall"]
#            0-2        3-5      6-8      9-11
# month = int(input())
# calculation = int((month%12) / 3)
# print(seasons[calculation])
