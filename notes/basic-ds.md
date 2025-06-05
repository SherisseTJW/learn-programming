# Basic Data Structures

## Lists (Arrays)

Outside of Python, most languages refer to Lists as Arrays. There is a difference between the two, but for now, you can consider them to be the same.

As the name suggests, Lists are just a list of various variables / values, otherwise referred to as *elements* when spoken to in the context of Lists. 

You can initialise a list as such: `example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`. This creates a list with numbers from 0 to 9 and assigns it to the variable `example_list`.

Lists are a nice way to contain multiple related elements together, and having lists also allow for several nice, cleaner, ways of doing certain things. For example, you could easily iterate through a list nicely:

```py
example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for value in example_list:
  print(value)
```

If you execute the above code, you will notice that each element in the list is printed one by one, in the order of left to right. 

However, sometimes, you may not want all the elements in a list. You may want just a single one or a few, but not all, of the elements. 
To retrieve a single element in a list, you would *index* the list. Each element in a list has a particular index associated with it, depending on where it lies in the order of the list. Take note that indices (the plural form of index) start from 0. 

```py
example_list = ["a", "b", "c"]

print(example_list[0]) # prints "a"
print(example_list[1]) # prints "b"
print(example_list[2]) # prints "c"
```

Note the syntax here, to index a list, you will have to do the following: `<variable_name>[<index>]`, replacing both "<variable_name>" and "<index>" to the appropriate value.

Python also has a concept called *List Comprehension* which you can look further into once you are confident and more familiar with the basics.

## Dictionaries

Consider a normal English Dictionary for example. You would look up a particular word, and the dictionary would have the meaning of the word right after it. In terms of the Programming Dictionary, the word would be referred to as a 'key' and the meaning would be referred to as the 'value'.

You can create a dictionary in Python as follows:

```py
example_dictionary = {
  "key": "value",
  "hello": "a greeting"
}
```

Then, if you want to get the *value* tied to a particular *key*, you would 'look up' the dictionary as follows: `<variable_name>[<key>]`. Notice the similarities in terms of indexing the list. For example:

```py
example_dictionary = {
  "key": "value",
  "hello": "a greeting"
}

print(example_dictionary["hello"])
```

"a greeting" will be printed to the terminal, which is the value associated with the key "hello". 

Note also that you will need the key to be of a `string` datatype. It is possible for the key to be of other datatypes, but that will be slightly more complex. Feel free to look it up however.

