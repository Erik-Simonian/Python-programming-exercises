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
