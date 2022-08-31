sex = input("Type in your biological sex: ")
hemo = float(input("Type in your hemoglobin in grams per litre (g/l): "))

if (sex.lower() == "female" and hemo < 117) or (sex.lower() == "male" and hemo < 134):
    print("Your hemoglobin is low.")
elif (sex.lower() == "female" and hemo > 175) or (sex.lower() == "male" and hemo > 195):
    print("Your hemoglobin is high.")
else:
    print("Your hemoglobin is normal")
