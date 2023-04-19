"""Question 21º
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps.
Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""


def answer_21():
    from math import sqrt
    position = [0, 0]
    while True:
        msg = input("Insert your command: ").split(" ")
        direction = msg[0]
        if direction == '':
            return int(round(sqrt(position[0] ** 2 + position[1] ** 2)))
        distance = int(msg[1])
        if direction == "UP":
            position[0] += distance
        elif direction == "DOWN":
            position[0] -= distance
        elif direction == "LEFT":
            position[1] -= distance
        elif direction == "RIGHT":
            position[1] += distance
        else:
            print("Please insert your command in a 'DIRECTION STEPS' format "
                  "or leave it blank if you want to get the result")


# print(answer_21())
# ----------------------------------------------------

# ----------------------------------------------------
"""Question 22:
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""


def answer_22():
    msg = input().split()
    dict_result = {}
    for i in msg:
        dict_result[i] = dict_result.get(i, 0) + 1
    sorted_dict = sorted(dict_result.items())
    for element in sorted_dict:
        result = ','.join(str(item) for item in element)
        print(result)


# answer_22()
# ----------------------------------------------

# ----------------------------------------------
"""Question 23:
    Write a method which can calculate square value of number
"""


def answer_23(n):
    return n ** 2


# print(answer_23(3))
# ----------------------------------------------

# ----------------------------------------------
"""Question 24:
    Python has many built-in functions, and if you do not know how to use it, 
    you can read document online or find some books. 
    But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function"""


# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
def answer_24(n):
    """Return square value of n."""
    return n ** 2


# print(answer_24.__doc__)
# ---------------------------------------------

# ---------------------------------------------
"""Question 25:
    Define a class, which have a class parameter and have a same instance parameter."""


class Dog:
    def __init__(self, name=None, breed=None):
        self.name = name
        self.breed = breed

    def __str__(self):
        if not self.breed:
            return f'{self.name} is a good dog.'
        else:
            return f'{self.name} is a {self.breed} dog.'


Bob = Dog('Bub', 'Husky')
print(Bob)