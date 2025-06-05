"""
Milestone 5 - Functions

Concepts:
1. Functions

Exercise:
Convert each of the previous exercises into that of a function
"""

intToCharMap = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "!",
    "5": "d",
    "6": "e",
    "7": "f",
    "8": "g",
    "9": "h",
    "10": "i",
    "11": "j",
    "12": "k",
    "13": "l",
    "14": "m",
    "15": "n",
    "16": "o",
    "17": "p",
    "18": " ",
    "19": "q",
    "20": "r",
    "21": "s",
    "22": "t",
    "23": "u",
    "24": "v",
    "25": "w",
    "26": "x",
    "27": "y",
    "28": "z",
}

A = ["9", "6", "13", "13", "16", "18", "25", "16", "20", "13", "5", "4"]


# Exercise 1
def exercise_1(x, y):
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)


exercise_1(10, 2)


# Exercise 2
def exercise_2(x, y, op):
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        print(x / y)
    elif op == "%":
        print(x % y)


exercise_2(10, 2, "+")


# Exercise 3
def exercise_3(x):
    for i in range(x):
        if x % 2 == 0:
            print(x)


exercise_3(10)


# Exercise 4
def exercise_4(intToCharMap, A):
    for element in A:
        print(intToCharMap[element])


exercise_4(intToCharMap, A)
