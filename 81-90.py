"""Question 81:
Please write a program to shuffle and print the list [3,6,7,8]."""


def answer_81():
    import random
    example_list = [3, 6, 7, 8]
    random.shuffle(example_list)
    print(example_list)


# answer_81()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 82:
Please write a program to generate all sentences where subject is in ["I", "You"] 
and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]."""


def answer_82():
    import itertools
    subject_list = ["I", "You"]
    verb_list = ["Play", "Love"]
    object_list = ["Hockey", "Football"]
    for subject, verb, an_object in itertools.product(subject_list, verb_list, object_list):
        msg = f'{subject}, {verb}, {an_object}'
        print(msg)


# answer_82()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 83:
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24]."""


def answer_83():
    num_list = [5, 6, 77, 45, 22, 12, 24]
    result = [x for x in num_list if x % 2 != 0]
    print(result)


# answer_83()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 84:
By using list comprehension, please write a program to print the list 
after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]."""


def answer_84():
    num_list = [12, 24, 35, 70, 88, 120, 155]
    result = [x for x in num_list if x % 5 != 0 and x % 7 != 0]
    print(result)


# answer_84()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 85:
By using list comprehension, please write a program to print the list 
after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]."""


def answer_85():
    num_list = [12, 24, 35, 70, 88, 120, 155]
    result = [x for (i, x) in enumerate(num_list) if i not in [0, 2, 4, 6]]
    print(result)


# answer_85()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 86:
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0."""


def answer_86():                                    # Numpy version is more efficient
    import numpy as np
    array = np.zeros((3, 5, 8), dtype=int)
    return array


# print(answer_86())
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 87:
By using list comprehension, please write a program to print the list 
after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]."""


def answer_88():
    num_list = [12, 24, 35, 70, 88, 120, 155]
    result = [x for (i, x) in enumerate(num_list) if i not in [0, 4, 5]]
    print(result)


# answer_88()
# -------------------------------------------------------

# -------------------------------------------------------
"""Question 89:
By using list comprehension, please write a program to print the list 
after removing the value 24 in [12,24,35,24,88,120,155]."""


def answer_89():
    num_list = [12, 24, 35, 24, 88, 120, 155]
    result = [x for x in num_list if x != 24]
    print(result)


# answer_89()
# -------------------------------------------------------

# -------------------------------------------------------



