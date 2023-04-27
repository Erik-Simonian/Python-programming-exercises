"""Question 31
Define a function that can accept an integer number as input
and print the "It is an even number" if the number is even, otherwise print "It is an odd number"."""


def answer_31(n):
    if n % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")


answer_31(11)
# ------------------------------------------------

# ------------------------------------------------
"""Question 32
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) 
and the values are square of keys."""


def answer_32():
    dict1 = dict()
    dict1[1] = 1
    for i in range(2, 4):
        dict1[i] = i ** 2
    print(dict1)


# answer_32()
# ---------------------------------------

# ---------------------------------------
"""Question 33
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) 
and the values are square of keys."""


def answer_33():
    dict1 = dict()
    for i in range(1, 21):
        dict1[i] = i ** 2
    print(dict1)


# answer_33()
# ----------------------------------------

# ----------------------------------------
"""Question 34
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
and the values are square of keys. The function should just print the values only."""


def answer_34():
    dict1 = dict()
    for i in range(1, 21):
        dict1[i] = i ** 2
    for k, v in dict1.items():
        print(v)


# answer_34()
# -----------------------------------------

# -----------------------------------------
"""Question 35:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
and the values are square of keys. The function should just print the keys only."""


def answer_35():
    dict1 = dict()
    for i in range(1, 21):
        dict1[i] = i ** 2
    for k in dict1.keys():
        print(k)


# answer_35()
# ----------------------------------

# ----------------------------------
"""Question 36:
Define a function which can generate and print a list 
where the values are square of numbers between 1 and 20 (both included)."""


def answer_36():
    result = [i ** 2 for i in range(1, 21)]
    print(result)


# answer_36()
# --------------------------------------------

# --------------------------------------------
"""Question 37:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list."""


def answer_37():
    result = [i ** 2 for i in range(1, 21)]
    print(result[:5])


# answer_37()
# ---------------------------------------------

# ---------------------------------------------
"""Question 38:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the last 5 elements in the list."""


def answer_38():
    result = [i ** 2 for i in range(1, 21)]
    print(result[-5:])


# answer_38()
# ----------------------------------------------

# ----------------------------------------------
"""Question 39
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list."""


def answer_39():
    result = [i ** 2 for i in range(1, 21)]
    print(result[5:])


# answer_39()
# ----------------------------------------------

# ----------------------------------------------
"""Question 40
Define a function which can generate and print a tuple 
where the value are square of numbers between 1 and 20 (both included). """


def answer_40():
    result = [i ** 2 for i in range(1, 21)]
    print(tuple(result))
