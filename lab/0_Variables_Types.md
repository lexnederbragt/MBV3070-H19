# Python 0: Variable Types (with focus on String and String methods)

* * * * *

There are many different kinds of programming languages. The language we are using today is python, which is an interpreted language. This means that we can write in code and it will be executed right away.

You can work with python in several ways, for example in the Jupyter Notebook, or you can write bits of code in a file and have that run by the python interpreter for you.

NOTE: a line anywhere in python that is preceded with a # is a comment and is ignored by python!

## How to do these exercises

In this exercise you will see python code in gray boxes. Try typing it in in the notebook, and see what happens. You will also see some questions being asked through the exercise, try to answer those while you are working through them. These questions will either be gone through during the exercise, or at the beginning of the next exercise.


## Getting started

Open a new Jupyter notebook and give it an appropriate name

Let's start very simply with some calculations:

```Python
print(2 + 2)
print(2*8)
```

We can also work with strings in python:

```Python
print("Hello world!")
print('Ada ' + 'Lovelace')
```
Strings can actually be added together.

Questions:
* Remove the space in Ada. What happens?  
* Replace the `+` with a comma. What happens?

## Python as a calculator
We are first going to use python as a simple calculator. Look at the operators that was shown for numbers at the lecture and test all of them.

## FIXME add suitable exercise

# String methods

Strings can be created by putting single, double or triple quotation marks around a piece of text. In this case we will be using the example string "ATG GGC ATG GGC" to demonstrate some string methods. Note that we recognize this string as a DNA sequence, but that for python, it simply is a string.

We will first count the number of Cs, replace a T with a U, split the text on whitespace and then find the occurrence of the first C.

```Python
print("ATG GGC ATG GGC".count("C"))
print("ATG GGC ATG GGC".replace("T", "U"))
print("ATG GGC ATG GGC".split())
print("ATG GGC ATG GGC".find("C"))
```

Questions:
* Why the first C is in position 6?  
* Can you explain the result of the `split` command?
* How would you find the number of Ts?    
* How would you find the position of the first T?   
* Can you remove the spaces in the string?  


## Using variables

In a programming situation, we usually have data that we want to do something to. We want to be able to work on the data without having to specify it directly, like we did with the numbers and "Hello World" above. Instead of specifying the data directly, we can use variables. Variables are names for data that we can do things twith. Many languages require us to specify what kind the data a variable should contain should be, like strings or numbers. Python does not require this, we can use them directly. This is called dynamic typing.

When you give a variable a value, you are assigning that value to that variable.

```Python
a = 1
print(a)
a = 'pigeon'
print(a)
a = 2 + 7
print(a)
```

Variables can be thought of being labels on values - you can move the label onto a different value. However, beware that Python does not assume any default values for variables - you have to assign them before use:

```Python
print(b)
```
**Question:** what happened when you typed in b, without assigning a value to b first?

## Strings are immutable

When working with strings, it is important to note that a string is immutable, it cannot be changed *in place*. Let's see what consequences this has:

```Python
first_string = "ATCATCATC"
first_string.replace("T", "U")
print(first_string)
```

As you can see, the string itself has not changed! If you want to modify a string, you need to assign the modified string to a new variable.

```Python
second_string = first_string.replace("T", "U")
print(second_string)
print(first_string)
```

As you can see, `second_string` now contains the modified string, while `first_string` remains the same.


## Dynamic and strong typing

Python also has what is called strong typing, this means that python will protest if you do something that the datatype does not allow for. As an example, what happens when we try to concatenate, i.e. combine two Python variables, string and integer:

```Python
string = "green"
number = 4
print(string + number )
```

## Type conversion

Sometimes a number can be interpreted as a text string when you need it to work as a number. This can be fixed by converting it to an integer (a whole number). We can also convert to decimal numbers - floats. These have a decimal point in them.

```Python
print(int('2') + 3)
print('2' + str('3'))
print(string + str(number))
```

### Task: Finding the GC content of a string

Let's say you have the string `"AGACTGAGGT"`. We would like to know how much GC there is in this string.

Below there is some partially complete code that will calculate this value. Copy the code into notepad, fill in the underscores, and copy-paste it into the python interpreter window.

```Python
DNA = ___
g = ___.count(___)
c = DNA.___(___)
gc_count = _ + _

print("GC count: ", ____)
```

**Question:** How much GC did the sequence have?
