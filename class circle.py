import math
 
 
class Circle:
    """A class to represent a circle with radius, area, and perimeter."""
 
    def __init__(self, radius):
        """Initialize the circle with a given radius."""
        self.radius = radius
 
    def calculate_area(self):
        """Compute and return the area of the circle (πr²)."""
        return math.pi * (self.radius**2)
 
    def calculate_perimeter(self):
        """Compute and return the perimeter/circumference of the circle (2πr)."""
        return 2 * math.pi * self.radius
 
 
# --- Example Usage ---
if __name__ == "__main__":
    # Prompt user for input
    try:
        user_radius = float(input("Enter the radius of the circle: "))
 
        if user_radius < 0:
            print("Radius cannot be negative.")
        else:
            # Instantiate the Circle object
            my_circle = Circle(user_radius)
 
            # Calculate and display results formatted to 2 decimal places
            print(f"Area of the circle: {my_circle.calculate_area():.2f}")
            print(
                f"Perimeter (Circumference): {my_circle.calculate_perimeter():.2f}"
            )
 
    except ValueError:
        print("Please enter a valid numerical value for the radius.")