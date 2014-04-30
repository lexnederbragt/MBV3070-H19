# Python 2 : Control flow - Boolean expressions, if statements, for loops and while.

## Boolean expressions

A basic element of programming is to be able to compare things, to see if they are equal or if one is larger or smaller than another. Many of these are similar to those found in other languages. 

```python
a = 1
b = 2
a == b # are the two the same?
a < b  # is a less than b?
a <= b # is a less than or equal to b?
a > b # is a larger than b?
a >= b # is a larger or greater than b?
a != b # 
```

Note, we can also test the results of doing something, like this:

```python
word = "Hello"
print len(word) < 10 # is the length of this word shorter than 10?
beatles=["George", "Ringo","John", "Paul"]
print len(beatles) == 4 # are there four members in beatles?
```

However, python has other equivalence test statements that are fairly
unique to python. To check whether an object is contained in a list :

```python
beatle="John"
beatles=["George", "Ringo","John", "Paul"]
print beatle in beatles # is John in the list beatles? 
print "Tom" in beatles # is there somebody in the list beatles called Tom?
```

We can also combine these with and, or and not. Let's see how this works:

```python
print beatle
print beatle in beatles
print len(beatles) == 4
print beatle in beatles and len(beatles) == 4 # is "John" in beatles, and are there four entries (members) in the beatles list?
print len(beatles) > 4
print beatle in beatles or len(beatles) > 4 # is "John" in beatles, or are are there more than 4 members in the list?
print len(beatles) > 3
print beatle in beatles or not len(beatles) >3
```
Q: write the boolean values (true or false) for each of these out on paper, and see if you get the same results as the computer.

## If statements

If statements are a way to select which parts of a piece of code that should be run depending on a condition, something that turns out to be true or false. An if statement consists of one if, zero or more elifs and maybe one else. Look at the if statement below, and figure out which parts of the code that would be run, and what would be printed in the end.

```python
i = 4
sign = "zero"
if i < 0:
	sign = "negative"
elif i > 0:
    sign = "positive"
else:
    print "Sign must be zero"
    print "Have a nice day"
print sign
```

Q: what is printed at the end when this piece of code is run?

Q: what would you need to change in order for this piece of code to print out "Sign must be zero" and "Have an nice day"?

Also note, Python uses ''indentation'' to delimit code blocks. The **indentation** above is NOT just to make things look pretty - it tells Python what the body of the if-statement is. This is true whenever we create any code blocks. 


### GCdecider.py - Figuring out if a DNA string has more or less than 50 % GC content.

Use the slides from last week, and look at the exercises from last week too. 

Define the following DNA string "ATGGCATGGCATGGC" as the variable DNA. Figure out the GC content of the string. If the GC content is above or equal to 50%, print out the following "GC content is above or equal to 50%", otherwise print out "GC content is below 50%". 

First, test this code out on the command line. Remember to indent! Press tab to indent and backspace to un-indent. Once you got it working there, save the code as a script (open New File to get a script shell, and remember to save the file as GCdecider.py) and run it using "Run Module". Also try to input another string and see what happens.


## For Loops with lists

**for** loops in python are used to iterate over sequences of things (they can be used for much more, but for now this definition will do). 

Let's start with a very simple list, and see how **for** behaves. 

```python
forlist = [1, 2 ,3,"a", 5, 9, "c"]
for elem in forlist:
	print elem
```

Let's try this with a list of words instead:

```python
words = ["green plants", "yellow sun", "blue water"]
for word in words:
	print word
```

Some things to note: each element will be used in the for loop in the order in which they appear in the list. Also, you absolutely need both the : and the tab, otherwise the for loop will not work. 

Q: what happens when you use a for loop to iterate over a string?

We can also create what is called nested for loops, this is when we have a loop within another one:

```python
numbers = [1, 2, 3, 4, 5]
words = ["green plants", "yellow sun", "blue water"]
for num in numbers:
	for word in words:
		print num, word
```
Explain to yourself what happens here. How are the elements from each of the two lists combined?

## Creating codons

Codons are triplets of nucleotides. Each of the three letters of the triplet can be one of four letters. In total, we have 64 codons, which equals 4*4*4. Can you think of how you can create a list of all codons using three nested for loops?


## For Loops with Dictionaries

With a list, then, it's clear that we can use the **in** keyword to indicate a list of things, and that we can create nested loops. How do we use use for loops with dicionaries? The clue here is to remember that the keys in a dictionary work like a list. 

```python
codondict = {}
codondict["UUU"] = "F"
codondict["ACA"] = "T"
codondict["CGG"] = "R"
for key in codondict:
    print key, codondict[key]
```
This way we see both the keys and their values.


## Combining for loops and if statements

A lot of the power in a programming language becomes apparent when we combine elements of the language. One very common thing to do is to use an if statement to decide what to do with something in a for loop. In this case, we will skip all words in a list that contains the character #. This is often used when we want to skip certain lines in files.

```python
words = ["gre#en", "yellow",  "sun", "#blue",  "water"]
for word in words:
	if "#" not in word:
		print word
```

Some comments: we here use **not** in front of **in**. This means that we are looking for sentences _without_ the # character. If we were to do it the other way around, we would end up with this code:

```python
words = ["gre#en", "yellow",  "sun", "#blue",  "water"]
for word in words:
	if "#" in word:
		pass
	else:
		print word
```

First of all, as you can see, this uses a lot more lines, and is inefficient due to this. Also, we are forced to use the instruction "pass" here - this instruction tells python to do nothing. If you need to use pass anywhere, your code should probably be changed.


While Loops
===========

With while loops, we iterate over something until a boolean expression goes from being false to being true. The first thing we need to make sure of before we start is that we have something that is true that can become false. It is very common to se counters used with while loops, i.e. a variable that counts up (or down), which eventually causes the expression to become false, and the loop terminates. 

```python
count = 0
while count < 9 :
	print 'The count is:', count
	count = count + 1
```

Here, we start with defining count as having the value 0. In the while loop, we first check if count is less than 9. If it is, we print what the count is, and increase the value of the count. Note - if we don't increase the value of count, it will never be equal to 9, and the loop will continue forever.

## Translate proteins

Last week we translated proteins manually. Now, we can do it a bit more efficiently. First, let's define a dictionary which can translate between them, and a DNA string to translate:

```python
codon_table = {"ATA":"I", "ATG":"M", "ACA":"T", \
               "AAC":"N", "CGA":"R", "CAG":"Q" }
dna = "ATGCAGAACATA"
```

First, define a new variable that will contain the protein string, and a counter with a value of 0. Next, use a while loop to iterate over triplets of the string. Use each triplet as a key in the dictionary, and add the resulting amino acid to the protein string (concatenate them using +). Finally, print the string. 

```python
protein = ""
counter = 0
while counter < len(dna) - 2:
	codon = dna[counter:counter + 3]
	protein = protein + codon_table[codon]
	counter = counter + 3
print protein
```

Q: it is often common to test things several times, especially when working in the interactive shell. What mistake regarding the counter can you imagine happening if you test several times?
 


## Homework: Testing if a list of DNA strings contains something else than DNA characters.

Sometimes you will see that a DNA string contains non-ATGC letters, these are most often IUPAC letters. In a situation where you want to translate DNA, these would have to be deconvoluted first. In this case we are just going to skip the strings that contain something else than DNA.

The list in this case is defined below:

```python
dnalist = ["ATTGAGGACCAG", "AGGNAAGGAT", "CGGATTTAGG", "PGATTAGGA"]
```
Figure out how you would iterate over this list, and skip any lines with non-ATGC characters.


