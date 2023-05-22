"""Question 61:
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)."""


def answer_61():
    n = int(input("Input a number bigger than 0:"))
    if n < 0:
        print("Aborting.The number must be bigger than 0")
    result = 0
    while n > 0:
        result += float(float(n) / (n + 1))
        n -= 1
    return result


# print(answer_61())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 62:
Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0)."""


def answer_62(n=int(input("Input a number bigger than 0:"))):
    if n <= 0:
        return 0
    else:
        return answer_62(n - 1) + 100


# print(answer_62())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 63:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console."""


know = {0: 0, 1: 1}


def answer_63(n):
    if n not in know:
        new = answer_63(n-1) + answer_63(n - 2)
        know[n] = new
    return know[n]


# print(answer_63(100))
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 64:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence 
in comma separated form with a given n input by console."""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def answer_64(n):
    result = [str(fib(n)) for n in range(0, n+1)]                  # Used str to print the result easier
    print(','.join(result))


# answer_64(10)
# -------------------------------------------------------

# -------------------------------------------------------
"""Question:
Please write a program using generator to print the even numbers between 0 and n in comma separated form 
while n is input by console."""


def gen_even(n):
    for x in range(0, n):
        if x % 2 == 0:
            yield x


def answer_65():
    n = int(input("Please insert a number bigger than 0: "))
    if n <= 0:
        print("Number must be bigger than 0")
        return
    result = []
    for i in gen_even(n):
        result.append(str(i))
    print(','.join(result))


# answer_65()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 66:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n 
in comma separated form while n is input by console."""


def gen_5_7(n):
    for x in range(1, n+1):
        if x % 5 == 0 and x % 7 == 0:
            yield x


def answer_66():
    n = int(input("Please insert a number(must be bigger than 0): "))
    if n <= 0:
        print("Number must be bigger than 0")
        return
    result = []
    for i in gen_5_7(n):
        result.append(str(i))
    print(','.join(result))


# answer_66()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 67:
Please write assert statements to verify that every number in the list [2,4,6,8] is even."""


def answer_67(list_1: list):
    for i in list_1:
        assert i % 2 == 0, "One or several items on the list are not even"
    print("All the element in the list are even")


even_list = [2, 4, 6, 8]
uneven_list = [3, 6, 9, 12]
# answer_67(even_list)
# answer_67(uneven_list)
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 68:
Please write a program which accepts basic mathematics expression from console and print the evaluation result."""


def answer_68():
    expression = input()
    print(eval(expression))


# answer_68()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 69:
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list."""


def answer_69(s_list: list, item):
    first_item = 0
    beyond_last = len(s_list)
    while True:
        if first_item == beyond_last:
            return -1
        mid_index = (first_item + beyond_last) // 2
        mid_item = s_list[mid_index]
        if mid_item == item:
            return mid_index
        if mid_item < item:
            first_item = mid_index + 1
        else:
            beyond_last = mid_index


lis = [1, 2, 3, 8, 5]
sorted_list = sorted(lis)
# print(sorted_list)
# print(answer_69(sorted_list, 5))
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 70
Please generate a random float where the value is between 10 and 100 using Python math module."""


def answer_70():
    import random
    return random.randrange(10, 101)


# print(answer_70())









