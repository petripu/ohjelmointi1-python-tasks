# program asks user to input medieval weight measurements
leiviska_n = float(input("Input leiviskäs.\n"))
naula_n = float(input("Input naulas.\n"))
luoti_n = float(input("Input luotis.\n"))

# weights
# leiviska = 20 naulas
# naula = 32 luotis
# luoti = 13.3 grams

# math time
first = ((leiviska_n * 20) * 32 * 13.3)
second = ((naula_n * 32) * 13.3)
third = luoti_n * 13.3

total = first + second + third
sum_kg = total / 1000
sum_gram = round(total % 1000, 2)

# print weight in kilograms and grams
print(f"Weight according to modern measurements: \n "
      f"{int(sum_kg)} kilograms and {sum_gram} grams.")
