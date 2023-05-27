"""Question 91:
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
after removing all duplicate values with original order reserved."""


def answer_91():
    result = []
    num_lust = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    for i in num_lust:
        if i not in result:
            result.append(i)
    return result


# print(answer_91())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 92:
Question:
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" 
which can print "Male" for Male class and "Female" for Female class."""


class Person:
    def __init__(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender


class Male(Person):
    def __init__(self, gender):
        Person.__init__(self, gender="Male")


class Female(Person):
    def __init__(self, gender):
        Person.__init__(self, gender="Female")


Human = Person("Male")
Man = Male("Male")
Female = Female("Female")
# print(Human.get_gender())
# print(Man.get_gender())
# print(Female.get_gender())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 93:
Please write a program which counts and prints the number of each character in a string input by console."""


def answer_93():
    msg = input()
    result = dict()
    for i in msg.lower():
        result[i] = result.get(i, 0) + 1
    for k, v in result.items():
        print(k, v)


# answer_93()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 94:
Please write a program which accepts a string from console and print it in reverse order."""


def answer_94():
    msg = input()
    print(msg[::-1])


# answer_94()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 95:
Please write a program which accepts a string from console and print the characters that have even indexes."""


def answer_95():
    msg = input()
    print(msg[::2])


# answer_95()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 96:
Please write a program which prints all permutations of [1,2,3]"""


def answer_96():
    import itertools
    print(list(itertools.permutations([1, 2, 3])))


# answer_96()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 97:
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?"""


def answer_97():
    start = 70
    finish = 94
    chicken = 35
    rabbits = 0
    while start != finish:
        chicken -= 1
        rabbits += 1
        start += 2
    print(f'Chickens: {chicken}, Rabbits: {rabbits}')


# answer_97()