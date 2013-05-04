# Python 1: Data Types: Lists, Sequence methods and Dictionaries

* * * * *

**Based on lecture materials by Milad Fatenejad, Joshua R. Smith, and Will
Trimble**

Modified by Karin Lagesen

One of the useful features of Python are its compound data types. The main two are lists and dictionaries.

## Lists

A list is an ordered, indexable collection of data. Lets say you have collected data on the AT content of some proteins:

```
AT_content:
0.53
0.4
0.3
0.8
0.6
```

So you could put that data into a list like this:

```python
at_content = [0.5, 0.4, 0.3, 0.8, 0.6]
```
We can add to the list by using append:

```python
at_content.append(0.4)
```
Let's say we have multiple values we want to add. These are kept in a separate list. There are two ways of adding to a list, append and extend. Let's try both:

```python
add_items = [0.1, 0.2]
at_content.append(add_items)
```
Q: what happened here?

Create a new list, at_content2, with the same numbers as before. Try doing the same as above with extend instead of append. What happens?

Q: would you use append or extend in this situation? Can you explain the difference between the two?


## Sequence methods

Lists and strings are both what we call "sequence types". These are types where the order of elements are important. These can be manipulated using the same methods. 

### Indices

We can access elements in lists and strings using indices. Python indices go from zero. Therefore, to find the value of the first item in at_content, we do this:

```python
at_content[0]
```

And to find the value of the third item

```python
at_content[2]
```

Lists can be indexed from the back using a negative index. The last item of at_content is accessed like this:

```python
at_content[-1]
1.0
```

and the next-to-last

```python
at_content[-2]
0.5
```

### Slicing

You can "slice" items from within a list. Lets say we wanted the second through fourth items from at_content

```python
at_content[1:4]
```

Or from the third item to the end

```python
at_content[2:]
```

and so on.

### The in operator

We can figure out if an element is in a sequence typed object, i.e. list or string with the in operator. 

Let's make a string and figure out whether certain things are in the string:

```python
teststring = "AUGUAGGGAUGG"
"A" in teststring
"AUG" in teststring
```
Q: can you find out if there were any Ts in this string? If there are none, what does that tell you?

### Concatenation

We can use the + sign to concatenate strings and lists.

First with lists:

```python
list1 = ["A", "B", "C", "D"]
list2 = [1, 2, 3, 4]
list1 + list2
```

and now for strings:

```python
text1 = "Watson"
text2 = "Crick"
text1 + text2
```

Q: what would you do to the strings above to introduce a space between Watson and Crick?

### Length, minimum and maximums

Sometimes you want to know how many items are in a list. Use the len command.

```python
len(at_content)
```

Next, we can find the minimum and the maximum of at_content.

```python
min(at_content)
max(at_content)
```

NOTE: when using min and max on a string, the min and max are found by looking at each character in lexicographic order. Lets try:

```python
text3 = "TtAaGgCc"
min(text3)
max(text3)
```
## Dictionaries

Recall our file data.dat which contained our current-voltage data and also
some metadata. We were able to import the data as a list, but clearly the
list type is not the optial choice for a data model. The dictionary is a
much better choice. A python dictionary is a collection of key, value
pairs. The key is a way to name the data, and the value is the data itself.
Here's a way to create a dictionary that contains all the data in our
data.dat file in a more sensible way than a list.

```python
dataDict = {"experiment": "current vs. voltage", \
                   "run": 47, \
                   "temperature": 372.756, \
                   "current": [-1.0, -0.5, 0.0, 0.5, 1.0], \
                   "voltage": [-2.0, -1.0, 0.0, 1.0, 2.0]}
```

This model is clearly better because you no longer have to remember that
the run number is in the second position of the list, you just refer
directly to "run":

```python
dataDict["run"]
47
```

If you wanted the voltage data list:

```python
dataDict["voltage"]
[-2.0, -1.0, 0.0, 1.0, 2.0]
```

Or perhaps you wanted the last element of the current data list

```python
dataDict["current"][-1]
1.0
```

Once a dictionary has been created, you can change the values of the data
if you like.

```python
dataDict["temperature"] = 3275.39
```

You can also add new keys to the dictionary.

```python
dataDict["user"] = "Johann G. von Ulm"
```

Dictionaries, like strings, lists, and all the rest, have built-in methods.
Lets say you wanted all the keys from a particular dictionary.

```python
dataDict.keys()
['run', 'temperature', 'current', 'experiment', 'user', 'voltage']
```

also, values

```python
dataDict.values()
 
[47,
 3275.39,
 [-1.0, -0.5, 0.0, 0.5, 1.0],
 'current vs. voltage',
 'Johann G. von Ulm',
 [-2.0, -1.0, 0.0, 1.0, 2.0]]
```

The help documentation has more information about what dictionaries can do.

Its worth mentioning that the value part of a dictionary can be any kind of
data, even another dictionary, or some complex nested structure. The same
is true about a list: they can contain complex data types.

Since tuples are immutable, they can be used as keys for dictionaries.
Lists are mutable, and therefore cannot.

When you architect software in python, most data will end up looking either
like a list or a dictionary. These two data types are very important in
python and you'll end up using them all the time.

Previous: [Variable types](0_Variables_Types.md) Next: [Flow control](2_Flow_Control.md)
