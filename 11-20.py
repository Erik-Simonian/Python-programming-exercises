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


print(answer_11())