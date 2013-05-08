# Python 0: Variable Types (with focus on String and String methods)

* * * * *

There are many different kinds of programming languages. The language we are using today is python, which is an interpreted language. This means that we can write in code and it will be executed right away. 

You can deal with python in two ways, either directly in an interpreter, or you can write bits of code in a file and have that run by the interpreter for you. 

NOTE: a line anywere in python that is preceeded with a # is a comment and is ignored by python!

## The python interpreter

Let's bring up the Python interpreter. You do this by starting IDLE on your windows machine. This is what you see when you open the program:
```python
   Python 2.7.3 (default, April 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
   Type "copyright", "credits" or "license" for more information.
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

Q: what happens if you don't include the space in Ada?

## Python as a calculator
We are first going to use python as a simple calculator. Look at the operators that was shown for numbers at the lecture and test all of them.

Q: What is the difference between 11/2 and 11.0/2.

## Creating your first script

In IDLE, go to "File" and click "New Window". You will get up a new window. Type in some of the commands that you typed in earlier when you used python as a calculator. Save the file as first.py. Then, go to the "Run" menu and click "Run Module".

NOTE: python scripts should be saved with the file ending .py. 

Q: what happened after you clicked "Run Module"? Did you see anything in the other window?
Q: try changing the file, save it and run again. What happened then?

Note: for the rest of the exercise we will work in the interactive shell.

# String methods

Strings can be created by putting single, double or triple quotation marks around a piece of text. In this case we will be using the example string "ATG GGC ATG GGC" to demonstrate some string methods.

We will first count the number of Cs, replace a T with a U, split the text on whitespace and then find the occurrence of the first C.

```python
   "ATG GGC ATG GGC".count("C")
   "ATG GGC ATG GGC".replace("T", "U")
   "ATG GGC ATG GGC".split()
   "ATG GGC ATG GGC".find("C")
```

Q: Why the first C is in position 5?

Q: How would you find the number of Ts?
Q: How would you find the position of the first T?

## Using variables

In a programming situation, we usually have data that we want to do something to. We want to be able to work on the data without having to specify it directly, like we did with the numbers and "Hello World" above. Instead of specifying the data directly, we can use variables. Variables contains data that we can do things to. Many languages require us to specify what kind the data a variable should contain should be, like strings or numbers. Python does not require this, we can use them directly. This is called dynamic typing.

When you give a variable a value, you are assigning that value to that variable. 

```python
   a = 1
   print a
   a = 'pigeon'
   print a
   a = 2 + 7 
   print a
```

Variables in Python are not typed as you can see. They can be thought of as being just names. However, beware that Python does not assume default variables - you have to assign them before use:

```python
   print b
```
Q: what happened when you typed in b, without assigning a value to b first?

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
