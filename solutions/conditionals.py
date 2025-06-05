"""
Milestone 2 - Conditionals

Concepts:
1. Boolean Datatypes
2. If, else if and else statements

Exercise:
Given two numbers, and a particular operation, print only the result of that operation on the two numbers.
"""

x = 2
y = 10
op = "+"  # Try changing to various other operations to test!

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

# You could also do the following instead of the above if, elif chain
if op == "+":
    print(x + y)

if op == "-":
    print(x - y)

if op == "*":
    print(x * y)

if op == "/":
    print(x / y)

if op == "%":
    print(x % y)
