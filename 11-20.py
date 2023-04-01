import numpy as np
import math

"""Question 11:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console."""


def answer_11():
    result = []
    number_list = [word for word in input().split(",") if int(word, 2) % 5 == 0]
    return number_list


# print(answer_11())
# ----------------------------------------

# ----------------------------------------
"""Question 12:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def answer_12():                                        # Not pretty but will do with a fixed range like that
    result = []
    for i in range(1000, 3001):
        string_i = str(i)
        if (int(string_i[0]) % 2 == 0) and (int(string_i[1]) % 2 == 0) and \
                (int(string_i[2]) % 2 == 0) and (int(string_i[3]) % 2 == 0):
            result.append(i)
    return result


print(answer_12())