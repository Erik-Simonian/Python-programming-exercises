"""Question 41:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line
and the last half values in one line. """


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
otherwise print "No". """


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
    from math import sqrt
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = map(lambda x: x ** 2, num_list)
    result = list(result)
    print(result)


# answer_45()
# -----------------------------------------

# -----------------------------------------
