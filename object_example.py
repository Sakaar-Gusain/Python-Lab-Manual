import math

# Define a class for Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Define a class for Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Define a class for Square (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Create objects of each shape and calculate their areas
def main():
    # Create three circle objects with different radii
    circle1 = Circle(3)
    circle2 = Circle(5)
    circle3 = Circle(7)
    
    # Create three rectangle objects with different dimensions
    rectangle1 = Rectangle(4, 5)
    rectangle2 = Rectangle(6, 8)
    rectangle3 = Rectangle(10, 12)
    
    # Create three square objects with different side lengths
    square1 = Square(4)
    square2 = Square(6)
    square3 = Square(8)
    
    # Calculate and print the areas of the circles
    print(f"Area of circle with radius 3: {circle1.area():.2f}")
    print(f"Area of circle with radius 5: {circle2.area():.2f}")
    print(f"Area of circle with radius 7: {circle3.area():.2f}")
    
    # Calculate and print the areas of the rectangles
    print(f"Area of rectangle with width 4 and height 5: {rectangle1.area():.2f}")
    print(f"Area of rectangle with width 6 and height 8: {rectangle2.area():.2f}")
    print(f"Area of rectangle with width 10 and height 12: {rectangle3.area():.2f}")
    
    # Calculate and print the areas of the squares
    print(f"Area of square with side 4: {square1.area():.2f}")
    print(f"Area of square with side 6: {square2.area():.2f}")
    print(f"Area of square with side 8: {square3.area():.2f}")

if __name__ == "__main__":
    main()
