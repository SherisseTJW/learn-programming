# Loops

Loops are nice when you want to repeat some line(s) of code multiple times. For example, if you wanted to print all numbers from 1 to 10, you could have 10 print statements like so:

```py
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
```

Granted, doing the above isn't too difficult, just troublesome. But, what if you wanted to print all numbers from 1 to 9999 for example. Would you have 9999 print statements one by one? 

A better way would be to use loops like so:

```py
for i in range(9999):
  print(i)
```

If you execute the above code, you will notice that you will get all numbers from 0 to 9998. There are several things to note here:
1. Notice that the last number printed is $9998$, and not $9999$. This is because we start from $0$, instead of $1$. (You can scroll all the way up, or change $9999$ to a smaller value to see that the first number printed is $0$)
  In other words, the code will repeat $9999$ times. 
2. You will notice that despite not changing the print statement, the number printed is increased by 1 each time.
  This is because what happens when you loop is that whatever the variable used in the loop is, in this case, `i`, it will be incremented (another term for increasing by 1) with each loop. A conditional is then evaluated to check that `i` is still smaller than the end value, $9999$ in this case.
3. We indent the print statement to denote a block of code. In other words, you can add more code to be executed with each loop similar to the conditional blocks.

This is an example of a numerical way of looping, that is, looping a fixed number of times.

Another way to loop, is a conditional loop, using `while`. An example is as follows:

```py
x = 0
while (x < 10):
  print(x)
  x = x + 1
```

The above loops while the conditional expression, `x < 10` in this case, evaluates to True. 
At the first loop, we print the value of the variable $x$, which is still $0$ at this time, then we increment $x$. 
We then evaluate if $x < 10$, which is True, and repeat the loop again.
This continues until $x$ has a value of $10$, in other words, after we loop 10 times, where $x < 10$, i.e., $10 < 10$ evaluates to False.

Notice that the above code is the equivalent of doing the following:

```py
for x in range(10):
  print(x)
```

You can of course add multiple `for` / `while` / conditional blocks within. This is also referred to as *nesting*.

An example is as follows:

```py
for x in range(10):
  if x < 5:
    print(x)
  else:
    print("x >= 5")
```
