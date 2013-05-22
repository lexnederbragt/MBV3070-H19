## Biopython ##

We are now going to explore the Biopython package a bit.

You can find a full listing of everything here:


http://www.biopython.org/XX

### Creating Seq objects ###


You are first going to figure out everything we can do with a Seq object. To find all the methods for a specifyc type or class, do help(classname).

```python
from Bio.Seq import Seq

help(Seq)

```

IGNORE all methods that begin with one or more underscores, those are "internal" to python. 

First, we are going to create a Seq object. To create a Seq object, we need a string and an alphabet. Strings are built in, so we only need to import an alphabet before creating our object.

```python
from Bio.Alphabet import IUPAC
my_seq = Seq("ATGGCC", IUPAC.unambiguous_dna)
```
Now, use some of the methods above on this string. 

Next, create an mRNA string instead. Make sure you use Us instead of Ts, and use the unambigous_rna alphabeth. Try out the various methods again. Can you find some that don't work when you are dealing with this string?

### Creating SeqRecord objects ###

SeqRecords hold not only the Seq, but also metadata. The only thing you need to create a Seq object however is a Seq, and a text string that will become the id.



### Using SeqIO ###


#### Reading in files ####

#### Looking at the contents ####

#### Writing out files ####

#### Creating custom convert to fasta script ####


