# Reading and Writing files

We are now going to see how we can read and write to files.

## Reading a file

To read a file, we need to have a file to read. First, we need to figure out where to save it. This we do by asking IDLE which directory it is currently working in:

```python
import os
os.getcwd()
```

os is what we call a module, and you will see more of those next week.

### Creating a coding table

Take the text below and save it in a textfile, using Notepad or something similar. Save it in the same location as you got above, with the name "translationtable.txt".

```
codon	amino_acid
TAG     *
TGA     *
TAA     *
GCT     A
GCA     A
GCC     A
GCG     A
TGT     C
TGC     C
GAC     D
GAT     D
GAG     E
GAA     E
TTC     F
TTT     F
GGA     G
GGG     G
GGT     G
GGC     G
CAC     H
CAT     H
ATA     I
ATC     I
ATT     I
AAG     K
AAA     K
CTA     L
CTC     L
CTT     L
TTG     L
TTA     L
CTG     L
ATG     M
AAT     N
AAC     N
CCC     P
CCT     P
CCA     P
CCG     P
CAA     Q
CAG     Q
AGG     R
AGA     R
CGA     R
CGG     R
CGT     R
CGC     R
TCA     S
AGT     S
TCG     S
TCC     S
TCT     S
AGC     S
ACA     T
ACT     T
ACG     T
ACC     T
GTA     V
GTC     V
GTT     V
GTG     V
TGG     W
TAC     Y
TAT     Y
```

We are now going to read in this file, and create a dictionary from it.

```python
fh = open("translationtable.txt", "r")
lines = fh.readlines()
fh.close()
```

Then, have a look at your new list (use print, for instance). How many entries does it contain? Can you tell whether the table is tab separated, or if there are just spaces in between the entries?

Next, we are going to use a for loop to read in all the entries into a dictionary, with the codons as the key, and the amino acid as the value. Note: below the code is incomplete. Figure out what is lacking (replace underscores with something else), and run it. 

```python
codon_table = {}
for line in _____:
	without_newline = line._____("\n", "")
	fields = without_newline.____()
	codon = fields[_]
	aminoacid = fields[_]
	codon_table[_____] = aminoacid
print codon_table
```

But note: you will see that you actually also get the first line of the file in here - this is no codon-amino acid pair. 

Q: How do you skip the first line when passing through the input file lines? 

Repeat the above code without the first line, and see what you get.

Q: can you figure out how many entries there are in the list?
Q: how would you iterate over the dictionary and show all codon-amino acid pairs? 

## Reading in a fasta file

We now have a codon to amino acid mapping dictionary. Now we need some DNA to translate.

Save the following in a file called "hbb.fsa".

```
>gi|28302128|ref|NM_000518.4| Homo sapiens hemoglobin, beta (HBB), mRNA
ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGA
GGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGC
AGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATG
CTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGC
TCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGAT
CCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCA
CCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCA
CTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACT
GGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGC
```

This is the mRNA sequence for hemoglobin subunit B. Let's try to translate that into protein.

First, we need to read in the file:

```python
fh = open("hbb.fsa", "r")
lines = fh.readlines()
fh.close()
```

So, now we have a list containing all of the lines in this file. Now we need to get this into one string containing the mRNA. This string will be contained in the variable mRNA. Again - some code is missing and has been replaced with underscores. Figure out how this should be, and run the code.

```python
mRNA = "" # create empty string to contain the mRNA
for line __ lines[__]:
	text = line.replace(____, __)
	mRNA = mRNA + ____
print text
```

Q: what are we removing from the input line, and why?

Q: One of the things that have been left for you to fill out is something after the name of the list in the for loop. What have we left out here? And, most importantly, why?

Q: after we have translated the DNA string, we will want to print it out to a new file, with the original heading. Where would we find that, and how could we store that for later?

## Translate proteins

So, now we have the translation table, and the DNA. Now we are going to translate it to protein. Again some text has been replaced by underscores.

```python
protein = ""
counter = 0
while _______ < len(mRNA) - _:
	codon = ____[counter:counter + 3]
	aminoacid = codon_table[_____]
	protein = ______ + aminoacid
	counter = counter + _
print protein
```

Q: what are we subtracting from the length of the mRNA? What is the consequence of this?

Q: what is the name what happens in the first line of the while loop, where we get the codon?

Q: what is the effect of what happens in the line inside of the while loop where protein is reassigned a value?

Q: what do we add to the counter at the end, and why? What would happen if we did not increase the value of the counter? What amount should we increase it with?

## Printing the results to file. 




