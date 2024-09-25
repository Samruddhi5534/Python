class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width

# Create a new Rectangle instance
newRectangle = Rectangle(12, 10)

# Print the area of the rectangle
print(newRectangle.rectangle_area())
