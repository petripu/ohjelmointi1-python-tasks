import math

circ_radius_str = input("Input circle radius: ")
circ_radius = float(circ_radius_str)
area = (math.pi)*(math.pow(circ_radius, 2))
print(f"Area of circle: {area:6.2f}")