# Reading and Writing files

## Files we need

Note: you have to save the file in the same directory that your cmd line window is in.


### Fasta file

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

### Codon translation file.

Save this file as "translationtable.txt".

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


We are now going to see how we can read and write to files. Note: use notepad to write the script, save it as translate.py and run it with python.

## Creating a codon table

We are now going to read in the "translationtable.txt" file, and create a dictionary from it.

```python
fh = open("translationtable.txt", "r")
lines = fh.readlines()
print lines.
fh.close()
```

Question: How many entries does it contain? (hint: how many lines do we get?)  
Question: Can you tell whether the table is tab separated, or if there are just spaces in between the entries?  

Next, we are going to use a for loop to read in all the entries into a dictionary, with the codons as the key, and the amino acid as the value. Note: below the code is incomplete. Figure out what is lacking (replace underscores with something else), and add it below the code you already have. 

```python
codon_table = {}
for line in lines:
    without_newline = line.replace("\n", "")
    fields = without_newline.split()
    codon = fields[0]
    aminoacid = fields[1]
    codon_table[codon] = aminoacid
print codon_table
```

But note: you will see that you actually also get the first line of the file in here - this is no codon-amino acid pair. 

Question: How do you skip the first line when passing through the input file lines?   

Repeat the above code without the first line, and see what you get.

Question: how would you iterate over the dictionary and show all codon-amino acid pairs?   
 
## Reading in a fasta file

We now have a codon to amino acid mapping dictionary. The file "hbb.fsa" that you saved above is the mRNA sequence for hemoglobin subunit B. Let's try to translate that into protein.

First, we need to read in the file (add this to your existing script file):

```python
fh = open("hbb.fsa", "r")
lines = fh.readlines()
fh.close()
```

So, now we have a list containing all of the lines in this file. Now we need to get this into one string containing the mRNA. This string will be contained in the variable mRNA. 

Below is the code necessary to read in the fasta file, with some text replaced with underscores. Figure out how this should be, and add it to your existing script.

```python
mRNA = "" # create empty string to contain the mRNA
for line __ lines[__]:
	text = line.replace(____, __)
	mRNA = mRNA + ____
print mRNA
```

Question: what are we removing from the input line, and why?

Question: One of the things that have been left for you to fill out is something after the name of the list in the for loop. What have we left out here? And, most importantly, why?

Question: after we have translated the DNA string, we will want to print it out to a new file, with the original heading. Where would we find that, and how could we store that for later?

## Translate proteins

So, now we have the translation table, and the mRNA. Now we are going to translate it to protein. What we do here is to slice the mRNA into codons and use them to look up the amino acid in the codon table. Then, we stick that onto the string that contains the protein. 

Insert this code below the rest of what you already have. 

```python
protein = ""
dnalen = len(mRNA)-2
numbers = range(0, dnalen, 3)  # start, stop, step size
for index in numbers:
    codon = mRNA[index:index+3]
    protein = protein + codon_table[codon]
print protein
```
Question: what are we subtracting from the length of the mRNA? What is the consequence of this?
Question: what happens in the two lines inside the for loop?

## Printing the results to file. 

Last, but not least, let's get this output to file. Let's first figure out how to get it nicely formatted. In this case, in our file we should have a header line followed by the amino acids, 60 per line. 

```python
output = lines[0] # we first add the header from the mRNA file
proteinlen = len(protein)
numbers = range(0, proteinlen, 60)  # start, stop, step size
for index in numbers:
    output = output + protein[index:index+60] + "\n"
print protein
```

So, now we have the output we want, and we can print it to a file. We first open it, then write to it, and then close it again.

```python
fo = open("protein.fsa", "w")
fo.write(output)
fo.close()
```

You can use the more command to look at the results.

Congratulations, you have now translated your very first protein!





