# Basics

## Datatypes

There are 3 main, basic, datatypes that we will go through in this section. 

1. `int`
2. `float`
3. `string`

You can think of `int` and `float` as numerical datatypes. 
The main difference is that `int` cannot have floating point values, that is values of the `int` datatypes can be $10$, $0$, $-10$ and so on. However, it cannot be $10.0$, $10.99$, $-0.00001$, etc.
In contrast, the `float` datatype has floating point values, for example, $10.0$, $10.99$, $-0.00001$, and so on.

As for `string`, it is simply a sequence of 0 or more characters. An easy way to identify values of the `string` datatype, is to look for the surrounding quotation marks. 
For example, the following are all `string` datatypes: `"hello"`, `"10"`, `"10.00"`, `-1.01`, and so on. 
Notice in the above example that even if we have numerical values, if it is surrounded by quotation marks, it will be treated as a `string` datatype.

It is important to keep track of what datatype a particular value is as the datatype affects what happens when you perform some operation on the value. 
For example, if you look at `int` or `float` datatypes, adding two values of this datatype will behave as expected in basic mathematics. That is, `10 + 10 = 20` for example.
However, if you have a `string` datatype, adding values of this datatype will instead give a different behaviour as follows: `"hello" + " " + "world" = "hello world"`. This is also referred to as *String Concatenation* which is what happens if you attempt to add strings together.

### Operations

Some basic arithmetic operations for `int` / `float` datatypes are as follows:
1. `+`: Addition
2. `-`: Subtraction
3. `*`: Multiplication
4. `/`: Division
5. `%`: Modulo

The first 4 should be pretty self-explanatory. The last operation, Modulo, simply returns you the remainder of the division operation. 
For example, `9 % 10 = 9`. If you think about it in terms of mathematics, $9 / 10$ gives you $0$ with a remainder of $9$.  

This Modulo operation is frequently used to determine if a number is divisible by another. 
Consider the following two values: $10$ and $2$, we know that $10$ is divisible by $2$, and in other words, we expect the remainder of $10 % 2$ to be $0$.
This same logic can be applied to other values.

## Printing

The basic method of returning results from your program, which also works as a way to debug the program, is to print the value. 

The easiest way is to print to *Standard Input (Stdin)*, which you can think of as your terminal / shell.
In Python, this can be done as follows:

```py
print("Hello World")
print(10)
print(10.09912)
print(-1212)
```

In essence, use `print(<some-value>)`, and replace the "<some-value>" within the round brackets with whatever value you want to print.

You can use this as a way to check if the result is as you expected, by printing the result.

## Comments

If you want to add some notes to your code, but don't want it to be executed or treated as code, you can use single-line, or multi-line comments. 
In Python, this can be done as follows:

```py
# This is a single-line comment, anything after the '#' will be treated as a comment
# For example, the below code is not executed
# print(10)

print("Hello World") # You can also put it at the end of the line if you want 

'''
In contrast, this is a multi-line comment. 
Anything in between the three single-quotes are treated as comments regardless of what line it is on
'''
```

## Variables

If you want to reuse certain values, you can also assign it to a variable, which can take on any datatype. 
In Python, you can do so as follows:
```py
x = 10
print(x)
```

If you run the above code, you can see that the value $10$ will be printed to the terminal instead of "x". Note however that this is because $x$ is treated as a variable. If you instead did the following:
```py
x = 10
print("x")
```

You will notice that the string "x" is printed rather than the value $10$. This is another example of making sure to keep track of what datatype you are using, and whether it is a constant value, or a variable. The resulting behaviour may differ if you do not keep track of this. 

Additionally, note that each variable can only hold 1 value at a time, and the value that it holds at a particular time is the latest when the code is executed top-down. In other words, if you have the following code:
```py
x = 10
print(x)

x = 20
print(x)
```

$10$ will be printed first, followed by $20$ in the next line. If you reversed the order, then $20$ will be printed first, followed by $10$ instead.

