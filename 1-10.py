import numpy as np

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


print(answer1_np())


def answer1():
    result = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)
    return result


print(answer1())
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
print(answer2(num))                     # of a desired number
