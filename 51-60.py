"""Question 51:
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area."""


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
# --------------------------------------------------

# --------------------------------------------------
"""Question 56:
Define a custom exception class which takes a string message as attribute."""


class CustomError(Exception):
    """CustomError
    Attributes:
        error_info -- information regarding Custom Error
    """
    def __init__(self, error_info):
        self.error_info = error_info


# err = CustomError("UU56Kl")
# print(err)
# --------------------------------------------------

# --------------------------------------------------
"""Question 57
Assuming that we have some email addresses in the "username@companyname.com" format, please write program 
to print the user name of a given email address. Both user names and company names are composed of letters only."""


def answer_57():
    name = input().split('@')
    print(name[0])


# answer_57()
# --------------------------------------------------

# --------------------------------------------------
"""Question 58:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program 
to print the company name of a given email address. Both user names and company names are composed of letters only."""


def answer_58():
    name = input().split('@')
    result = name[1].split('.')
    print(result[0])


# answer_58()
# --------------------------------------------------

# --------------------------------------------------
"""Question 59
Write a program which accepts a sequence of words separated by whitespace as input 
to print the words composed of digits only."""


def answer_59():
    import re
    print(re.findall("\d+",input()))


# answer_59()
# --------------------------------------------------

# --------------------------------------------------
"""Question 60
Print a unicode string "hello world"."""


def answer_60():                                                    # In Python 3 all strings are unicode
    import re                                                       # so here's "hello world" written
    msg = "hello world"                                             # with unicode characters instead
    result = (re.sub('.', lambda x: r'\u % 04X' % ord(x.group()), msg))
    print(str(result))


# answer_60()
