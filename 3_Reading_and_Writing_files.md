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

Next, we are going to use a for loop to read in all the entries into a dictionary, with the codons as the key, and the amino acid as the value. Note: below the code is incomplete. Figure out what is lacking, and run it. 

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

But note: you will see that you actually also get the first line of the file in here - this is no codon-amino acid pair. How do you skip the first line when passing through the input file lines? Repeat the above code without the first line, and see what you get.

## 


