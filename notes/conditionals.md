# Conditionals

## Boolean Datatypes

For Conditionals, we first need to learn another datatype: `Boolean`

`Boolean` datatypes are special in that they only have two possible values: `True` and `False`

You can obtain Boolean values by either initialising it directly, i.e., `x = True`, or by evaluating some inequality. 

Examples of inequality are: $>, >=, <, <=, ==, !=$. From left to right, greater than, greater than or equal to, lesser than, lesser than or equal to, equal to, not equal to

Notice that a single equal sign, i.e., `x = 10` is an assignment operation, whereas 2 equal signs, i.e, `x == 10` is an equality expression, that is, there is some evaluation of the result here.

## If, Else if (Elif) and Else

The basic Conditionals are performed via the following statements: `If`, `Elif` and `Else`. 

In Python, this can be done as follows:
```py
if True:
  print("Yay")

print("Something")
```

You will notice that both "Yay" and "Something" is printed. If you instead did the following:
```py
if False:
  print("Booo")

print("Something")
```
Now, you will notice that only "Something" is printed.

In other words, the code after the conditional is executed only if whatever is after the `If` evaluates to `True`. Notice that we require the result of the evaluation to be a Boolean value. 
This makes more sense if you consider that saying something like "If 10 + 5" doesn't quite make sense even in English. Instead, it will only make sense if you say something like "If 10 + 5 is equal to 15", or in Python: `If (10 + 5 == 15)`

When working with conditionals, you can also do the following:
```py
x = 10
if x == 10:
  print("10")
else:
  print("Not 10")
```

In which case, only 1 of the two print statements will be executed. `print("Not 10")` is executed only if the conditional in the If block, i.e., `x == 10` evaluates to False. 

If you wanted to evaluate more conditionals, you could also add `elif` in the middle like so:

```py
x = 10
y = 5
if x == y:
  print("x == y")
elif y == 5:
  print("y is 5")
else:
  print("x is not equal to y AND y is not equal to 5")
```

Here, "y is 5" only prints if x is not equal to y and y is indeed equal to 5. That is, if x is equal to y, "y is 5" does not print even if y is indeed equal to 5. 
In other words, in an entire if, elif, else block, only 1 of none of the code are executed. Multiple blocks cannot execute.

If you wanted multiple blocks to execute, you would have to start a different if block like so:

```py
x = 10
y = 5
if x > y:
  print("x > y")

if y == 5:
  print("y is 5")
```

In the above, both "x > y" and "y is 5" is printed to the terminal.

Here, notice the indentation of the print statements. This denotes to Python the start, and end of blocks of code. For example, given the following:

```py
x = 10
if x == 10:
  print("This executes")
  print("x is 10")
  print("I'm still here!")
```

If you run the above code, all three print statements are printed.
