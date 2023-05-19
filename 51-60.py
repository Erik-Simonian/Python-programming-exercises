"""Question 51:
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area. """


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14


# circle = Circle(5)
# print(circle.area())
# --------------------------------------------------

# --------------------------------------------------
"""Question 52:
Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area."""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# rect = Rectangle(3, 4)
# print(rect.area())
# --------------------------------------------------

# --------------------------------------------------
"""Question 53
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as 
argument. Both classes have an area function which can print the area of the shape 
where Shape's area is 0 by default."""


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


# square = Square(5)
# print(square.area())
# --------------------------------------------------

# --------------------------------------------------
"""Question 54
Please raise a RuntimeError exception."""

error = False
# error = True                                          # Uncomment to access the raise statement.
if error:                                               # Had to use the switch to make the rest of the code reachable
    raise RuntimeError('Error')
# --------------------------------------------------

# --------------------------------------------------
"""Question 55
Write a function to compute 5/0 and use try/except to catch the exceptions."""


def answer_55():
    return 5/0


def answer_55_test():
    try:
        answer_55()
    except ZeroDivisionError:
        print("Can't divide by zero!")
    except error:
        print("Error")
    finally:
        print("Finished")


# answer_55_test()
