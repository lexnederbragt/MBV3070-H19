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

Next, create an mRNA string instead. Make sure you use Us instead of Ts, and use the unambigous_rna alphabeth. Try out the various methods again. 

Q: Can you find some methods that work with DNA, but not mRNA?

### Creating SeqRecord objects ###

SeqRecords hold not only the Seq, but also metadata. The only thing you need to create a Seq object however is a Seq, and a text string that will become the id.

First, let's import them and see what help says about them:

```python
from Bio.SeqRecord import SeqRecord

help(SeqRecord)

```

...something about the methods here....

Let's create a SeqRecord:

```python
seq_record = SeqRecord(seq = my_seq, id = "MyID")
```

Print seq_record, and see what you come up with.

Now, let's read in SeqRecords from a genbank file and play with them:

### Using SeqIO ###

First, from now on we are working in a script file. So, the code below goes in a file that you save and then run.

Second, download this genbank file and save it in the same place as you saved other files. Save it as hbb_one.gbk. This file contains only one genbank entry - we are going to have a look at it.

```python
from Bio import SeqI0 # Have to import the module to have access to it.

fh = open("hbb_one.gbk", "r")
one_gbk = SeqIO.parse(fh, "genbank").next()
fh.close()

#below here you type in the methods you want to test. The object you
#are testing them on are one_gbk


```

Remember the methods that you saw using help earlier? Try some of them out by writing them in after where you close the file.

Q: can you find out X
Q: can you find out Y



### name_with_taxonomy.py ###

We are now going to create a script that will let us print out fasta sequences with an ID which begins with the organism name.

#### Reading in files ####

We first need a genbank file to work with. Download this one and save it as hbb.gbk

Next, save the following in a script file named name_with_taxonomy.py

```python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fh = open("hbb.gbk", "r")

for record in SeqIO.parse(fh, "genbank"):
    print record.id

fh.close()
```

Run it, and you will see the ids of the sequences in the hbb.gbk file printed on screen.

#### Creating a new id ####

Now, can you remember how you could get at the taxonomy of a sequence? Add a print statement after `print record.id`, so that you will first get one line with the id of the sequence, and one with the taxonomy.

As you can see, these are now just strings. Strings can be added together. Try having both on one line, with a print in front.

We are now going to create a new id for each entry. This can be done by doing this:

```python
   # Note: we are now inside the for loop
   record.id = TAXONOMY + record.id
```

Add a print statement inside the for loop after you have assigned a new value to record.id, so that you get to see what this is.


#### Writing out files ####

We are now going to write this out to file. We now need to also have an out file open. 


```python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fh = open("hbb.gbk", "r")
fo = open("hbb_taxonomy.fsa", "w")

for record in SeqIO.parse(fh, "genbank"):
    record.id = TAXONOMY + record.id
    SeqIO.write(fo, record, "fasta")

fh.close()
fo.close()
```


Congratulations, you have now created your own custom conversion script!