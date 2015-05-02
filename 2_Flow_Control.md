# Python 2 : Control flow - Boolean expressions, if statements and for loops.
## Howto

Note: for this exercise, use Notepad to write things into a file, save it under a name that you choose (remember to have the file ending with .py), and then run it with 'python <yourchosenfilename>.py'.

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

if i < 0: #the if statement begins here
	sign = "negative"
elif i > 0:
    sign = "positive"
else:
    print "Sign must be zero"
    print "Have a nice day" # and ends here
print sign
```

Question: what is printed at the end when this piece of code is run?

Question: what would you need to change in order for this piece of code to print out "Sign must be zero" and "Have an nice day"?

Also note, Python uses ''indentation'' to delimit code blocks. The **indentation** above is NOT just to make things look pretty - it tells Python what the body of the if-statement is. This is true whenever we create any code blocks. 


### Task: GCdecider.py - Figuring out if a DNA string has more or less than 50 % GC content.

Use the slides from last week, and look at the exercises from last week too. 

The goal for this task is to figure out if a piece of DNA contains more than 50% GCs or not. This basically means counting the number of Gs and Cs and figuring out if these together make up more than 50% of the number of nucleotides in the string.

Below is skeleton script that will do this. Save this in a file that you will name GCdecider.py. Figure out what each line of code should do, and fill in the missing text. Try to run it, does it work? 

```python
___ = "ATGGCATGGCATGGC"
g = dna._____("G")
c = ___.count(_)
gc = (g + c)*100.0/___(____)
if ______:
    print "GC content is above or equal to 50%"
else:
    print "GC content is below 50%"
```

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


range() - create list of numbers
===========

With the range command, we can create a list of numbers that we can use in for loops:

```python
numbers = range(10)
print numbers
```

With this way of writing it, range will produce numbers from 0 to the number in the parenthesis. 

We can also specify where it should start, and also the step size between the numbers:

```python
numbers = range(0, 12, 3)  # start, stop, step size
print numbers
```

With this construct, we have a way of grabbing each codon in a piece of DNA:

```python
dna = "ATCATCATCATCATC"
dnalen = len(dna)
numbers = range(0, dnalen, 3)  # start, stop, step size
print numbers
for index in numbers:
    print dna[index:index+3]
```
We can now use this to translate a protein.

## Translate proteins

Last week we translated proteins manually. Now, we can do it a bit more efficiently. First, let's define a dictionary which can translate between them, and a DNA string to translate:

```python
codon_table = {"ATA":"I", "ATG":"M", "ACA":"T", \
               "AAC":"N", "CGA":"R", "CAG":"Q" }
dna = "ATGCAGAACATA"
```

First, define a new variable that will contain the protein string. Then we need a list of numbers that we can use to slice the string with. Next, we use a for loop to iterate over triplets of the string. WE use each triplet as a key in the dictionary, and add the resulting amino acid to the protein string (concatenate them using +). Finally, print the string. 

```python
protein = ""
dnalen = len(dna)
numbers = range(0, dnalen, 3)  # start, stop, step size
for index in numbers:
    codon = dna[index:index+3]
    protein = protein + codon_table[codon]
print protein
```

Question: what happens if the DNA string does not have 


## Homework: Testing if a list of DNA strings contains something else than DNA characters.

Sometimes you will see that a DNA string contains non-ATGC letters, these are most often IUPAC letters. In a situation where you want to translate DNA, these would have to be deconvoluted first. In this case we are just going to skip the strings that contain something else than DNA.

The list in this case is defined below:

```python
dnalist = ["ATTGAGGACCAG", "AGGNAAGGAT", "CGGATTTAGG", "PGATTAGGA"]
```
Figure out how you would iterate over this list, and skip any lines with non-ATGC characters.


