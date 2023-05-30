"""Question 41:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line
and the last half values in one line."""


def answer_41():
    num_tuple = tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(num_tuple[:5])
    print(num_tuple[5:])


# answer_41()
# -----------------------------------------------------

# -----------------------------------------------------
"""Question 42:
Write a program to generate and print another tuple whose values 
are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)."""


def answer_42():
    num_tuple = tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    result = []
    for i in num_tuple:
        if i % 2 == 0:
            result.append(i)
    result = tuple(result)
    print(result)


# answer_42
# -------------------------------------------

# -------------------------------------------
"""Question 43:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", 
otherwise print "No"."""


def answer_43():
    msg = str(input())
    msg = msg.lower()
    if msg == "yes":
        print("Yes")
    else:
        print("No")


# answer_43()
# --------------------------------------------

# --------------------------------------------
"""Question 44:
Write a program which can filter even numbers in a list by using filter function. 
The list is: [1,2,3,4,5,6,7,8,9,10]."""


def answer_44():
    def check_even(number):
        if number % 2 == 0:
            return True
        return False
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter(check_even, numbers)
    result = list(result)
    print(result)


# answer_44()
# -------------------------------------------

# -------------------------------------------
"""Question 45:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]."""


def answer_45():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = map(lambda x: x ** 2, num_list)
    result = list(result)
    print(result)


# answer_45()
# -----------------------------------------

# -----------------------------------------
""""Question 46:
Write a program which can map() and filter() to make a list whose elements 
are square of even number in [1,2,3,4,5,6,7,8,9,10]."""


def answer_46():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sqr = map(lambda x: x ** 2, num_list)
    sqr = list(sqr)
    result = filter(lambda x: x % 2 == 0, sqr)
    result = list(result)
    print(result)


# answer_46()
# ----------------------------------------------

# ----------------------------------------------
"""Question 47:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)."""


def answer_47():
    result = filter(lambda x: x % 2 == 0, range(1, 21))
    result = list(result)
    print(result)


# answer_47()
# ----------------------------------------------

# ----------------------------------------------
"""Question 48:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)."""


def answer_48():
    result = map(lambda x: x ** 2, range(1, 21))
    result = list(result)
    print(result)


# answer_48()
# -----------------------------------------------

# -----------------------------------------------
"""Question 49:
Define a class named American which has a static method called printNationality."""


class American:
    @staticmethod
    def print_nationality():
        print("American")


# a_person = American()
# American.print_nationality()
# a_person.print_nationality()
# -------------------------------------------------

# -------------------------------------------------
"""Question 50:
Define a class named American and its subclass NewYorker."""


class AnAmerican:
    pass


class NewYorker(AnAmerican):
    pass


# person_1 = AnAmerican()
# person_2 = NewYorker()
# print(type(person_1))
# print(person_2.__class__.__mro__)
