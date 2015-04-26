# Python 0: Variable Types (with focus on String and String methods)

* * * * *

There are many different kinds of programming languages. The language we are using today is python, which is an interpreted language. This means that we can write in code and it will be executed right away. 

You can work with python in two ways, either directly in an interpreter, or you can write bits of code in a file and have that run by the interpreter for you. 

NOTE: a line anywere in python that is preceeded with a # is a comment and is ignored by python!

## The python interpreter

Let's bring up the Python interpreter. You do this by first starting a command window on your windows machine. You do this by pressing the start button, and typing in 'cmd' in the search box and pressing enter. The result is a black window where you can type in things after a arrow symbol. Type in the word 'python', and press enter. This is what you see when you open the program:

```python
Python 2.7.8 |Anaconda 2.1.0 (64-bit)| (default, Jul  2 2014, 15:12:11) [MS
500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://binstar.org
>>>
```

See the three >? You type in your commands after that.

The interpreter can be used as a calculator:

```python
   print 2 + 2
   print 2*8
```

We can also work with strings in python:

```python
   print "Hello world!"
   print 'Ada ' + 'Lovelace'
```
Strings can actually be added together.

Question: Remove the space in Ada. What happens?

## Python as a calculator
We are first going to use python as a simple calculator. Look at the operators that was shown for numbers at the lecture and test all of them.

Question: What is the difference between 11/2 and 11.0/2?

Exit the interpreter by typing in Ctlr-D.

## Creating your first script

Open notepad. You will get up a new window. Type in some of the commands that you typed in earlier when you used python as a calculator. Notice which directory your command window is in (it says where you can type in the command). Save the file as first.py in the same directory. Then, go to the command window. Run the program by typing in

```python
  python first.py
```

NOTE: python scripts should be saved with the file ending .py. 

Question: What happened in the command window?
Question: try changing something in the file, save it and run again. What happens?

Note: for the rest of the exercise we will work in the interactive shell.

# String methods

Strings can be created by putting single, double or triple quotation marks around a piece of text. In this case we will be using the example string "ATG GGC ATG GGC" to demonstrate some string methods.

We will first count the number of Cs, replace a T with a U, split the text on whitespace and then find the occurrence of the first C.

```python
   print "ATG GGC ATG GGC".count("C")
   print "ATG GGC ATG GGC".replace("T", "U")
   print "ATG GGC ATG GGC".split()
   print "ATG GGC ATG GGC".find("C")
```

Question: Why the first C is in position 6?
Question: How would you find the number of Ts?
Question: How would you find the position of the first T?

## Using variables

In a programming situation, we usually have data that we want to do something to. We want to be able to work on the data without having to specify it directly, like we did with the numbers and "Hello World" above. Instead of specifying the data directly, we can use variables. Variables contain data that we can do things to. Many languages require us to specify what kind the data a variable should contain should be, like strings or numbers. Python does not require this, we can use them directly. This is called dynamic typing.

When you give a variable a value, you are assigning that value to that variable. 

```python
   a = 1
   print a
   a = 'pigeon'
   print a
   a = 2 + 7 
   print a
```

Variables can be thought of being labels on values - you can move the label onto a different value. However, beware that Python does not assume any default values for variables - you have to assign them before use:

```python
   print b
```
Question: what happened when you typed in b, without assigning a value to b first?

## Strings are immutable

When working with strings, it is important to note that a string is immutable, it cannot be changed. Let's see what consequences this has:

```python
   first_string = "ATCATCATC"
   first_string.replace("T", "U")
   print first_string
```

As you can see, the string itself has not changed! If you want to modify a string, you need to assign the modified string to a new variable.

```python
   second_string = first_string.replace("T", "U")
   print second_string
   print first_string
```

As you can see, second_string now contains the modified string, while first_string remains the same.


## Dynamic and strong typing

Python also has what is called strong typing, this means that python will protest if you do something that the datatype does not allow for. As an example, what happens when we try to concatenate, i.e. combine two Python variables, string and integer:

```python
   string = "green"
   number = 4
   print string + number 
```

## Type conversion

Sometimes a number can be interpreted as a text string when you need it to work as a number. This can be fixed by converting it to an integer (a whole number). We can also convert to decimal numbers - floats. These have a decimal point in them.

```python
   print int('2') + 3
   print '2' + str('3')
   print string + str(number)
```

Next: [Data Types](1_Data_Types.md)
