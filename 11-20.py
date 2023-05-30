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
    number_list = [word for word in input().split(",") if int(word, 2) % 5 == 0]
    return number_list


# print(answer_11())
# ----------------------------------------

# ----------------------------------------
"""Question 12:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line."""


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
LOWER CASE 9"""


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


# print(answer_15(9))
# ----------------------------------------

# ----------------------------------------
"""Question 16:
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9"""


def answer_16():
    result = [x for x in input().split(",") if int(x) % 2 != 0]
    return ",".join(result)


# print(answer_16())
# -----------------------------------------------------

# -----------------------------------------------------
"""Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""


def answer_17():
    net = 0
    while True:
        msg = input('How much do you want to deposit/withdraw?(type "end" to stop and check your account.)')
        if msg[0].lower() == "d":
            amount = int(msg[2:])
            net += amount
        elif msg[0].lower() == "w":
            amount = int(msg[2:])
            net -= amount
        if msg.lower() == "end":
            return net


# print(answer_17())
# -------------------------------------------

# --------------------------------------------
"""Question 18:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""


def answer_18():
    import re
    symbols = re.compile("[$#@]")
    pattern = re.compile("[A-Za-z0-9]+")
    for item in input(str("Enter password: ")).split(','):
        if pattern.search(item) and 6 <= len(item) <= 12 and symbols.search(item):
            print(item)
        else:
            pass


# answer_18()
# ----------------------------------------------------

# ----------------------------------------------------
"""Question 19:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, 
age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jonny,17,91
Jonny,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jonny', '17', '91'), ('Jonny', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]."""


def answer_19():
    from operator import itemgetter
    result = []
    while True:
        msg = input()
        if not msg:
            break
        result.append((tuple(msg.split(','))))

    print(sorted(result, key=itemgetter(0, 1, 2)))


# answer_19()
# --------------------------------------------

# --------------------------------------------
"""Question 20

Question:
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n."""


def answer_20(n):
    value = 0
    while value < n:
        value += 1
        if value % 7 == 0:
            yield value


# for i in answer_20(100):
#   print(i)
