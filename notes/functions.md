# Functions

## Basic Functions

Functions are more complicated to think about. You can think of them as blocks of code which requires a specific line of code to execute. 

Functions are denoted as follows:

```py
def example_function():
  print("This is an example function")
```

If you just execute the above code, you will notice that nothing happens. Instead, you will have to *call* the function like so:

```py
def example_function():
  print("This is an example function")

example_function()
```

Now, you can see that the print statement is executed. That is, if you do not specifically 'call' them, the block of code within functions are not executed. Furthermore, note the indentation now. That means that everything indented appropriately will be treated as part of the function code.

It is important now to know that functions are 'black-boxes'. This means that, by default, any variable declared (created) outside the function cannot be used within the function. It is unfortunate that Python will allow you to do the following:

```py
x = 10

def test():
  print(x)

test()
```

However, take note that Python tries its best to allow new beginners / developers to do what they want to do, which includes adding support for things like the above when most, if not all other languages will yell at you (throw an error) for attempting to do the same thing. 

There are various reasons for why this isn't really the best thing to do, which you may see if you explore coding in Python further, however, for now, as best practice, we will pretend that the above does not work. 

Instead, we will go through something called *Function Arguments* that allow developers to 'pass in' variables / values from outside the function into the function.

## Function Arguments

When defining functions, we can define additional 'arguments' that the function can accept. You can think of these arguments as Inputs to the black box, I.e., something that you put into the box.

```py
def example_function(argument_1, argument_2):
  print(argument_1)
  print(argument_2)

example_function(10, 20)
```

If you run the above code, you will see that both "10" and "20" are printed, and in that specific order. In other words,

1. The order when passing in arguments is matched with the order of the arguments declared. That is, if you switch 10 and 20, i.e. instead call the function as follows: `example_function(20, 10)`, you will see that now, "20" is printed first, followed by "10"
2. You can change the value passed in when calling the function, without having to adjust anything within the function

## Returning from Functions

Returning (Exiting) from Functions can happen in one of two ways:
1. Reaching the end of the block of code in the function
2. Specifically returning from the function via code

All the above examples use the first method to exit the function. The second method is as follows:

```py
def example_return_function():
  print("Returning in the next line!")
  return
```

Note the explicit addition of the `return` keyword here. More specifically, this allows you to do the following:

```py
def example_return_function(x):
  if x == 10:
    return
  else:
    print("Something or another")
    return

example_return_function(5)
```

In the above, you will see that "Something or another" is printed before exiting. In contrast, if you change the value passed in to be $10$, you will see that nothing is printed.

The second method also allows you to provide an output value from the function. That is, you can do the following:

```py
def example_return_function(x):
  return x + 10

y = example_return_function(5)
print(y)
```

Executing the above code, you will see $15$ printed. Combining this with conditionals, you can thus alter what value you return from the function depending on some conditional. 

For example,

```py
def example_return_function(x, operation):
  if operation == "+":
    return x + 10
  else:
    return x

y = example_return_function(30, "+")
print(y)
```
