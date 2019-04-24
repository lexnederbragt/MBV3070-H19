# Reading and Writing files

## Files we need

Note: you have to save the file in the same folder that your notebook is in.


### Fasta file

The sequence below is the mRNA sequence for hemoglobin subunit B. Save it in a file called `hbb.fna`: Select `New` from the top right of the window, then `Text File`. Paste the sequence below and save it under the right name. `fna` stands for 'fasta nucleic acid', where 'fasta' refers to the "fasta file format":"https://en.wikipedia.org/wiki/FASTA_format".

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

Save this file as `translationtable.txt`.

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


We are now going to see how we can read and write to files.

## Creating a codon table

We are now going to read in the `translationtable.txt` file, and create a dictionary from it.

```Python
fh = open('translationtable.txt', "r") # the translation table file
lines = fh.readlines()
print(lines)
print(len(lines))
fh.close()
```

Question: How many entries does it contain?   
Question: Can you tell whether the table is tab separated, or if there are just spaces in between the entries?  

Next, we are going to use a for loop to read in all the entries into a dictionary, with the codons as the key, and the amino acid as the value.

In a new codecell, use the previous program without the `print` staements, and add the following code:

```Python
codon_table = {}
for line in lines:
    without_newline = line.replace("\n", "")
    fields = without_newline.split()
    codon = fields[0]
    aminoacid = fields[1]
    codon_table[codon] = aminoacid
```

Check the results:

```Python
print(codon_table)
```

But note: you will see that you actually also get the first line of the file in here - this is no codon-amino acid pair.

Question: How do you skip the first line when passing through the input file lines? Hint: this involves slicing.   

Repeat the above code without the first line, and see what you get.

Question: how would you iterate over the dictionary and show all codon-amino acid pairs?   

## Reading in a fasta file

We now have a codon to amino acid mapping dictionary. Remember that the file `hbb.fna` that you saved above is the mRNA sequence for hemoglobin subunit B. Let's try to translate that into protein.

First, we need to read in the file. Create a new codecell with a code to read the content of the `hbb.fna` file, skips the first line and removes the newlines so that you end up with the DNA sequence as one string in a variable called `mRNA`.


<!--
```Python
mRNA = "" # create empty string to contain the mRNA
for line __ lines[__]:
	text = line.replace(____, __)
	mRNA = mRNA + ____
print(mRNA)
```

```Python
mRNA = "" # create empty string to contain the mRNA
for line in lines[1:]:
	text = line.replace("\n","")
	mRNA = mRNA + text
print(mRNA)
```
-->

Question: after we have translated the DNA string, we will want to print it out to a new file, with the original heading. What would you need to change to your program so we could store the heading for later?

## Translate proteins

Now we have the translation table, and the mRNA. Now we are going to translate it to protein. What we do here is to slice the mRNA into codons and use them to look up the amino acid in the codon table. Then, we stick that onto the string that contains the protein.

The program below has some underscores in it that has to be replaced. A lot of this are things you saw in the previous exercises. Figure out what goes instead of the underscore, copy the code into a new codecell and finihs it.

```Python
protein = ""
dnalen = len(____)-2
numbers = range(0, ____, 3)  # start, stop, step size
for index in _______:
    codon = mRNA[_____:index+3]
    aa = codon_table[_____]
    protein = _______ + aa
print(protein)
```
Question: what are we subtracting from the length of the mRNA? What is the consequence of this?
Question: what happens in the three lines inside the for loop?

## Printing the results to file.

Last, but not least, let's get this output to file. Let's first figure out how to get it nicely formatted. In this case, in our file we should have a header line followed by the amino acids, 60 per line.

```Python
output = lines[0] # we first add the header from the mRNA file
proteinlen = len(protein)
numbers = range(0, proteinlen, 60)  # start, stop, step size
for index in numbers:
    output = output + protein[index:index+60] + "\n"
print(output)
```
Question: can you identify where in the code the fasta description line comes from?

So, now we have the output we want, and we can print it to a file. We first open it, then write to it, and then close it again. Again, remove any print statements. `faa` indicates 'fasta amino acid'.

```Python
fo = open('hbb.faa', "w") # output file name
fo.write(output)
fo.close()
```
Regarding output file name: be sure to use the name of a file that does not exist! You can find the file in the Notebook browser, click on the filename to see its content.

Congratulations, you have now translated your very first protein!
