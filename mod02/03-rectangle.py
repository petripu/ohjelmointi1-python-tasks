sqr_width = float(input("Input square width: "))
sqr_height = float(input("Input square height: "))

# calculate square circumference
sqr_cir = (sqr_height*2) + (sqr_width*2)

# calculate square area
sqr_area = (sqr_height) * (sqr_width)

print(f"Circumference of square is  {sqr_cir:6.2f}")
print(f"Area of square is {sqr_area:6.2f}")