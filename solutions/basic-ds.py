"""
Milestone 4 - Basic Data Structures

Concepts:
1. List datatypes (Arrays)
2. Dictionaries

Exercise:
Given a list of Strings $A$, and a dictionary mapping Strings to Characters,
print the resultant string of characters mapped to by the dictionary.
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

for element in A:
    print(intToCharMap[element])
