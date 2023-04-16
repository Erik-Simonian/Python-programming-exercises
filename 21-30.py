"""Question 21º
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps.
Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""


def answer_21():
    from math import sqrt
    position = [0, 0]
    while True:
        msg = input("Insert your command: ").split(" ")
        direction = msg[0]
        if direction == '':
            return int(round(sqrt(position[0] ** 2 + position[1] ** 2)))
        distance = int(msg[1])
        if direction == "UP":
            position[0] += distance
        elif direction == "DOWN":
            position[0] -= distance
        elif direction == "LEFT":
            position[1] -= distance
        elif direction == "RIGHT":
            position[1] += distance
        else:
            print("Please insert your command in a 'DIRECTION STEPS' format "
                  "or leave it blank of you want to get the result")


print(answer_21())