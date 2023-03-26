import numpy as np
import math

"""Question 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""


def answer1_np():                           # Numpy Version
    array = np.array([])                    # Had to add a couple of extra steps
    for i in np.arange(2000, 3201):         # to get that comma between elements.
        if i % 7 == 0 and i % 5 != 0:
            array = np.append(array, i)
    a = np.array(array, int)
    result = a.tolist()
    return result


# print(answer1_np())


def answer1():
    result = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)
    return result


# print(answer1())
# ---------------------------------------------------------

# ---------------------------------------------------------

"""Question 2:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""


def answer2(n):
    if n == 0:
        return 1
    return n * answer2(n - 1)


# user_input = int(input())             # Uncomment for and input option
# print(answer2(user_input))
num = 8                                 # You can change "num" value the factorial 
# print(answer2(num))                     # of a desired number
# -----------------------------------------------------

# -----------------------------------------------------

"""Question 3:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is 
an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""


def answer3(n):
    result = {}                                     # result = dict() also works here
    for i in range(1, n+1):
        result[i] = i * i
    return result


# print(answer3(8))
# print(answer3(input))
# ----------------------------------------------------

# ----------------------------------------------------

"""Question 4:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple 
which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""


def answer4(n):
    n_list = [n]
    tuple_split = n.split(", ")
    n_tup = tuple(tuple_split)
    return n_list, n_tup


# print(answer4("34,67,55,33,12,98"))
# print(answer4(input()))
# -----------------------------------------------------

# -----------------------------------------------------

"""Question 5:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""


class AnswerFive:
    def __init__(self):
        self.msg = None

    def getString(self):
        self.msg = input()

    def printString(self):
        print(self.msg.upper())


# obj = AnswerFive()
# obj.getString()
# obj.printString()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 6:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""


def answer_6():
    c = 50
    h = 30
    result = []
    item_list = [i for i in input().split(",")]
    for item in item_list:
        result.append(str(int(round(math.sqrt(2 * c * float(item) / h)))))

    print(",".join(result))


# answer_6()
# -----------------------------------------------------------

# -----------------------------------------------------------
"""Question 7:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""


def answer_7(x, y):
    result = [col * row for col in range(x) for row in range(y)]
    array = np.array(result)
    answer = np.reshape(array, (x, y))
    return answer


print(answer_7(3, 5))


