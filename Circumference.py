import math
 
def calculate_circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    return 2 * math.pi * radius
 
r = 4
c = calculate_circumference(r)
print(f"The circumference of a circle with radius {r} is {c:.2f}")