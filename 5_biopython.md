## Biopython ##

We are now going to explore the Biopython package a bit.

You can find a full listing of everything here:

http://biopython.org/DIST/docs/api/


### Creating Seq objects ###


NoteL for now we are working in the interactive shell.

You are first going to figure out everything we can do with a Seq object. To find all the methods for a specifyc type or class, do help(classname).

```python
from Bio.Seq import Seq
help(Seq)
```

Now scroll through them. Space gets you further down in the file, b gets you back up again. q will let you quit.IGNORE all methods that begin with one or more underscores, those are "internal" to python. 

As you can see, there are lots of methods that are available. 

** A note on self **

When you see methods described here, you will always as a paremeter to the function see the word **self**. This just means that you specify that you are doing whatever you are doing on the object whose method you are using. This also means that you do not type in anything instead of self. I.e. if you see the method this_is_a_fake_method(self), you don't need to type in anything between the paranthesis. If you instead have this_is_a_fake_method(self, par1, par2), you will need to put in 2 parameters, corresponding to par1 and par2.


First, we are going to create a Seq object. To create a Seq object, we need a string and an alphabet. Strings are built in, so we only need to import an alphabet before creating our object.

```python
from Bio.Alphabet import IUPAC
my_seq = Seq("ATGGCC", IUPAC.unambiguous_dna)
```
Now, use the following methods on the my_seq seq: transcribe(), translate(), complement(), reverse_complement()

Next, create an mRNA string instead. Make sure you use Us instead of Ts, and use the unambigous_rna alphabeth. Try out the various methods again. 

Q: Can you find some methods that work with DNA, but not mRNA?

### We can use normal string methods on Seq ###

Figure out how to do the following:

- how long my_seq is
- what the first letter is
- all of the sequence, except the first and last letter

Notice the difference between the results from the last two.


### Creating SeqRecord objects ###

SeqRecords hold not only the Seq, but also metadata. 

First, let's import them and see what help says about them:

```python
from Bio.SeqRecord import SeqRecord
help(SeqRecord)

```

Many of these are simply the same methods as for Seq.

Let's create a SeqRecord. The only thing you need to create a Seq object however is a Seq, and a text string that will become the id.

```python
seq_record = SeqRecord(seq = my_seq, id = "MyID")
```

Print seq_record, and see what you come up with.

Let us create a slightly more complicated one:

```python
protein_record = SeqRecord(Seq("MKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVF", \
                    IUPAC.protein), \
                    id="YP_025292.1", name="HokC", \
                    description="toxic membrane protein")
```

You will now try to access all of the attributes that this object has. Hint: to get to the id, you would type in `protein_record.id`.



### Using SeqIO ###

First, from now on we are working in a script file. So, the code below goes in a file that you save and then run.

Second, download this genbank file and save it in the same place as you saved other files. Save it as macaca.gbk. This file contains only one genbank entry - we are going to have a look at it.

```python
from Bio import SeqIO # Have to import the module to have access to it.

fh = open("macaca.gbk", "r")
macaca = SeqIO.parse(fh, "genbank").next()
fh.close()

# Below here you type in the things I specify 
# you should look at later. The object you
# are testing them on are macaca


```

We are now going to try looking at the annotations in this object. In the script, write `print macaca.annotations` after the comment, save and run.

Q: Can you recognize what this is?
Q: Can you from this figure out what you would have to do to get at the organism information.


### name_with_organism.py ###

We are now going to create a script that will let us print out fasta sequences with an ID which begins with the organism name.

#### Reading in files ####

We first need a genbank file to work with. Download [mb.gbk](this one) and save it as mb.gbk

Next, save the following in a script file named name_with_organism.py

```python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fh = open("mb.gbk", "r")

for record in SeqIO.parse(fh, "genbank"):
    print record.id

fh.close()
```

Run it, and you will see the ids of the sequences in the mb.gbk file printed on screen.

#### Creating a new id ####

Now, can you remember how you could get at the organism of a sequence? Add a print statement that will print this out
 on the line after `print record.id`, so that you will first get one line with the id of the sequence, and one with the organism name.

As you can see, these are now just strings. Strings can be added together. 

In this case, we have two words in our string, the genus name and the species name. We will only use the species name.

Q: In a string with two words, what do you use to get at only the last word?

We are now going to create a new id for each entry. This can be done by doing this:

```python
   # Note: we are now inside the for loop
   organism = record.annotations['organism']
   species_name = organism.split()[1]
   record.id = species_name + "_" + record.id
```

Add a print statement inside the for loop after you have assigned a new value to record.id, so that you get to see what this is.


#### Writing out files ####

We are now going to write this out to file. We now need to also have an out file open. 

Look at this example and figure out which portions of this you need in your own script:

```python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fh = open("fake_file_name.gkb", "r")
fo = open("fake_file_name.fsa", "w")

for record in SeqIO.parse(fh, "genbank"):
    SeqIO.write(fo, record, "fasta")
fh.close()

```

Congratulations, you have now created your own custom conversion script!