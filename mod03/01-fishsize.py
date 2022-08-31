kuha_size_caught = float(input("Input kuha lenght in cm: "))

kuha_size_min = 37
kuha_size_missing = kuha_size_min - kuha_size_caught
if kuha_size_caught < kuha_size_min:
    print(f"Kuha too small by {round(kuha_size_missing, 2)} cm, "
          f"please release it so it can keep growing!")
