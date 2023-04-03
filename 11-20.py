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


# print(answer_12())
# ----------------------------------------

# ----------------------------------------
"""Question 13:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""


def answer_13():
    dict_result = {"LETTERS": 0, "DIGITS": 0}
    msg = input()
    for i in msg:
        if i.isalpha():
            dict_result["LETTERS"] += 1
        elif i.isdigit():
            dict_result["DIGITS"] += 1
    for k, v in dict_result.items():                                # Could just print twice but I like this more
        print(k, v)


# answer_13()
# --------------------------------------------

# --------------------------------------------
"""Question 14:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""


def answer_14():
    dict_result = {"UPPER CASE": 0, "LOWER CASE": 0}
    msg = input()
    for i in msg:
        if i.isupper():
            dict_result["UPPER CASE"] += 1
        elif i.islower():
            dict_result["LOWER CASE"] += 1
    for k, v in dict_result.items():
        print(k, v)


# answer_14()
# ---------------------------------------

# ---------------------------------------
"""Question 15:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106"""


# def answer_15(n):
#    tot = ""
#    result = 0
#    for element in range(4):
#        tot += str(n)
#        result += int(tot)
#    return result

answer_15_dict = {}


def answer_15(n, r=4):                                      # Recursion version of answer_15
    tot = ""
    for i in range(r):
        tot += str(n)
        answer_15(n, r-1)
        if tot not in answer_15_dict:
            answer_15_dict[i] = int(tot)
    return sum(answer_15_dict.values())


print(answer_15(9))

