# Python 1: Data Types: Lists, Sequence methods and Dictionaries

* * * * *

**Written by Karin Lagesen**

Note: we are using the interactive shell here, as in the previous exercise. 

Note: if you want to repeat something that you have already typed in, try the arrow buttons on your keyboard.


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

### Sorting a list 

A list can be sorted in place, like this:

```python
   at_content.sort()
   print at_content
```


### Adding to a list

We can add to the list by using append:

```python
at_content.append(0.4)
print at_content
```
Let's say we have multiple values we want to add. These are kept in a separate list. There are two ways of adding to a list, append and extend. Let's try both:

```python
add_items = [0.1, 0.2]
at_content.append(add_items)
print at_content
```

Question: what happened here?

Create a new list, at_content2, with the same numbers as in at_content. Try doing the same as above with extend instead of append. What happens?

Question: would you use append or extend in this situation? Can you explain the difference between the two?

## Sequence methods

Lists and strings are both what we call "sequence types". These are types where the order of elements are important. These can be manipulated using the same methods. 

### Indices

Let's first recreate the at_content list:

```python
at_content = [0.5, 0.4, 0.3, 0.8, 0.6]
print at_content
```

We can access elements in lists and strings using indices. Python indices go from zero. Therefore, to find the value of the first item in at_content, we do this:

```python
print at_content[0]
```

And to find the value of the third item

```python
print at_content[2]
```

Lists can be indexed from the end using a negative index. The last item of at_content is accessed like this:

```python
print at_content[-1]
```

and the next-to-last

```python
print at_content[-2]
```

### Slicing

You can "slice" items from within a list. Lets say we wanted the second through fourth items from at_content

```python
print at_content[1:4]
```

Or from the third item to the end

```python
print at_content[2:]
```

and so on.

### Task: Slicing 

Create a list called newlist which contains the numbers below: 

[0.5, 0.6, 0.8, 0.4, [0.1, 0.2]]

1. Get python to print the list that is inside the list.
2. Get python to print last element of the list inside the list.

### The in operator

We can figure out if an element is in a sequence typed object, i.e. list or string with the in operator. 

Let's make a string and figure out whether certain things are in the string:

```python
teststring = "AUGUAGGGAUGG"
print "A" in teststring
print "AUG" in teststring
```
Question: can you find out if there were any Ts in this string? If there are none, what does that tell you?

### Concatenation

We can use the + sign to concatenate strings and lists.

First with lists:

```python
list1 = ["A", "B", "C", "D"]
list2 = [1, 2, 3, 4]
print list1 + list2
```

and now for strings:

```python
text1 = "Watson"
text2 = "Crick"
print text1 + text2
```

Question: what would you do to the strings above to introduce a space between Watson and Crick?

### Length, minimum and maximums

Sometimes you want to know how many items are in a list. Use the len command.

```python
print len(at_content)
```

Next, we can find the minimum and the maximum of at_content.

```python
print min(at_content)
print max(at_content)
```

NOTE: when using min and max on a string, the min and max are found by looking at each character in lexicographic order. Let's try:

```python
mytext = "TtAaGgCc"
print min(mytext)
print max(mytext)
```

### Task: Open reading frame G count

Given the DNA string "CGAGATGGCAGCACGAGCACAGGA", do the following:

1. Store the string as the variable dna.
2. Figure out how to find where the open reading frame starts (starts with ATG). Save the value in the variable number.
3. Slice the string, so that only the open reading frame remains (no stop codons in the string, so just stop at the end). Save this as the variable orf.
4. Count and print the number of Gs in the open reading frame.

## Dictionaries

A python dictionary is a collection of key, value pairs. The key is a way to name the data, and the value is the data itself.

Today we are going to create a dictionary that contains part of the genetic code. We are going to take this table here and create a dictonary from it:

```
ATA                I
ATG                M
ACA                T
AAC                N
CGA                R
CAG                Q
```

Now we are going to create a dictionary from this, using the codons as keys and the one-letter amino acids as values. This will enable us to translate from DNA to protein.


```python
codon_table = {"ATA":"I", "ATG":"M", "ACA":"T", "AAC":"N", "CGA":"R", "CAG":"Q" }
```
Dictionaries are very good for storing data where the relationship between elements matter. In this case, the important thing is the relationship between the codon and the amino acid. The order of the codons do not matter.

So, let's manipulate this dictionary a bit. 

### Lookup

A dictionary is often used to look up the value of a certain key. In this case, let's find out which amino acid you would get from ATA:

```python
print codon_table["ATA"]
```

Let's try another one, CCG:

```python
print codon_table["CCG"]
```
Oups -  that did not work did it? Can you figure out what went wrong?

### The in operator, and adding to the list

From the last example it seems it would be useful to be able to tell whether a key is part of a dictionary. We can do this using the in operator, just like we did for lists:

```python
print "AAC" in codon_table
print "CCG" in codon_table
```

So, CCG is not in the table. Let's add it. CCG codes for P, proline. Adding a new key-value pair to a dictionary simply means defining it:

```python
codon_table["CCG"] = "P"
```

Let's now look at what we have in the dictionary:

```python
print codon_table
```

As you can see the new codon is in there. Let's redo the test, just to make sure our eyes are not deceiving us:

```python
print "CCG" in codon_table
```

###Keys and values

We can access all the keys and the values of a dictionary using the keys() and the values() methods:

```python
print codon_table.keys()
print codon_table.values()
```
## Finding out more

All python data types like lists, strings and dictionaries have help documentation available in the interpreter. Try typing in

```python
help(dict)
```

The python webpages also have a lot of information, and a very good tutorial:

[The python tutorial](http://docs.python.org/2/tutorial)

A lot of the material taught in this course draws heavily on this book:

[Python for Bioinformatics by Sebastian Bassi](http://www.amazon.com/Bioinformatics-Chapman-Mathematical-Computational-Biology/dp/1584889292)


## Homework

There are two tasks that you may do. In both cases, you will create text document (word is fine here) containing the following:

1. The code itself
2. A copy of what appears in the terminal when you run it.

Send this to me.

### ORF finding

Below is part of a python script that is meant to translate a DNA string into RNA, find the open reading frame in it (only look for the start codon AUG), find the stop codon (in this case UAA) and print the string from that position until the start of the stop codon.

In the code there are words missing. Fill them in.

```python
   	seq = "ATTATGAGATTACAGAGCTAAGAC"   
	mrna = seq._______("T", "U")
	start = mrna.find("___")
	stop = mrna.____("UAA")
	print mrna[_____:stop]
```

Use notepad to create the completed script, and save it as orf.py. Run it on the command line like this: 'python orf.py'. 

### CG frequency

CpG islands are regions of sequence that contain higher than expected number of CpG (CG) dinucleotides (this is a C followed by a G, i.e. the substring CG). CpG islands are found near or in 40% of all promoters in mammalian genomes. We will now create a script that will allow us to calculate the CG frequency in a given string.

Define the DNA string CGCTACGGACGTAGCCAGCGA.

Create a script that will calculate the percent of CG dinucleotides in the string. Note, a string that contains N nucleotides, contains N-1 dinucleotides.

Hint: look at how we calculated AT content in the lecture.


Previous: [Variable types](0_Variables_Types.md)
