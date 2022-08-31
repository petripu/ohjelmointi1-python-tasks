cabinclass = input("Syötä hytin nimi: ")

if cabinclass.lower() == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif cabinclass == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif cabinclass == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif cabinclass == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
