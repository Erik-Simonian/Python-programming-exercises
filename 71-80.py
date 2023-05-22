"""Question 71:
Please generate a random float where the value is between 5 and 95 using Python math module."""


def answer_71():
    import random
    return random.randrange(5, 96)


# print(answer_71())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 72:
Please write a program to output a random even number between 0 and 10 inclusive 
using random module and list comprehension."""


def answer_72():
    import random
    return random.choice([x for x in range(11) if x % 2 == 0])


# print(answer_72())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 73:
Please write a program to output a random number, which is divisible by 5 and 7, 
between 0 and 1000 inclusive using random module and list comprehension."""


def answer_73():
    import random
    return random.choice([x for x in range(1001) if x % 5 == 0 and x % 7 == 0])


# print(answer_73())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 74:
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive."""


def answer_74():
    import random
    return random.sample(range(100, 201), 5)


# print(answer_74())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 75:
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive."""


def answer_75():
    import random
    return random.sample([x for x in range(100, 201) if x % 2 == 0], 5)


# print(answer_75())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 76:
Please write a program to randomly generate a list with 5 numbers, 
which are divisible by 5 and 7 , between 1 and 1000 inclusive."""


def answer_76():
    import random
    return random.sample([i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0], 5)


# print(answer_76())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 77:
Please write a program to randomly print a integer number between 7 and 15 inclusive."""


def answer_77():
    import random
    print(random.randint(7, 16))


# answer_77()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question: 78
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"."""


def answer_79():
    import zlib
    msg = b'hello world!hello world!hello world!hello world!'
    compressed_msg = zlib.compress(msg)
    decompressed_msg = zlib.decompress(compressed_msg)
    print(compressed_msg)
    print(decompressed_msg)


# answer_79()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 80:
Please write a program to print the running time of execution of "1+1" for 100 times."""


def answer_80():
    from timeit import Timer
    result = Timer('for i in range (100):1+1')
    print(result.timeit())


# answer_80()