## Biopython ##

We are now going to explore the Biopython package a bit.

You can find a full listing of everything here:

http://biopython.org/DIST/docs/api/


### Working with Seqs ###


Note: for now we are working in the interactive shell.

You are first going to figure out what we can do with a string stored as a Seq. To find all the methods for a specify type, do help(type_name).

```Python
from Bio.Seq import Seq
help(Seq)
```

Now scroll through the help. You go down by pressing the space bar, and up by scrolling. If you want to quit, press q. 

Find the method that is named \_\_init\_\_ . This method is the one that is run every time you create a Seq, and in this one you will find which kinds of data that you need to have to create one. This means that every Seq will have these set, i.e. have something there. 

Question: what kinds of data do you have to have to create a Seq?  

Everything you see in the help is a method . As you can see, there are lots of methods that are available. However, you should only use the ones without one or two underscores in the beginning.  

#### A note on self ####

When you see methods described here, you will always as a parameter to the function see the word **self**. This just means that you specify that you are doing whatever you are doing on the object whose method you are using. This also means that you do not type in anything instead of self. I.e. if you see the method this_is_a_fake_method(self), you don't need to type in anything between the parenthesis. If you instead have this_is_a_fake_method(self, par1, par2), you will need to put in 2 parameters, corresponding to par1 and par2.

First, we are going to create a new Seq. To do that, we need a string and an alphabet. Strings are built in, so we only need to import an alphabet before creating our object.

```Python
from Bio.Alphabet import IUPAC
my_seq = Seq("ATGGCC", IUPAC.unambiguous_dna)
```
Now, use the following methods on the my_seq seq: my_seq.transcribe(), my_seq.translate(), my_seq.complement(), my_seq.reverse_complement().

Next, create an mRNA string instead. Make sure you use Us instead of Ts, and use the unambigous_rna alphabeth. Try out the various methods again. 

Question: Can you find some methods that work with DNA, but not mRNA?

### We can use normal string methods on Seq ###

Remember how you did the "normal" string operations? Look at the previous exercises if you are uncertain.

Many of the normal string methods work on Seq objects.

Figure out how to do the following:

- how long my_seq is
- what the first letter is
- all of the sequence, except the first and last letter

Question: can you see a difference in the results between the results from the first two and the last?  


### Creating SeqRecord objects ###

SeqRecords hold not only the Seq, but also metadata. 

First, let's import them and see what help says about them:

```Python
from Bio.SeqRecord import SeqRecord
help(SeqRecord)

```
Question: can you figure out what kind of data you need to have to create a SeqRecord? 

As you can see, many of the methods are simply the same methods as for Seq.

Let's create a SeqRecord. The only thing you need to create a SeqRecord is a Seq, and a text string that will become the id.

```Python
seq_record = SeqRecord(seq = my_seq, id = "MyID")
```

Print seq_record, and see what you come up with.

Let us create a slightly more complicated one:

```Python
protein_record = SeqRecord(Seq("MKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVF",
                    IUPAC.protein),
                    id="YP_025292.1", name="HokC",
                    description="toxic membrane protein")
```

You will now try to access all of the data that is stored in this SeqRecord. Hint: to get to the id, you would type in `protein_record.id`.


### Using SeqIO ###

First, from now on we are working in a script file. So, the code below goes in a file that you save and then run with python27 if you are on the windows machines at the university.

Second, go to this page [this genbank file](macaca.gbk). Click on "Raw", you should now get it up in a separate window. Copy the contents and  and save it in a file in the same place as you saved other files. Save it as macaca.gbk. This file contains only one genbank entry - we are going to have a look at it.

Take the code shown below, and save it in a file. We are going to explore the genbank file by gradually expanding on this script. 


```Python
import sys
from Bio import SeqIO # Have to import the module to have access to it.

fh = open(sys.argv[1], "r")
gbk = SeqIO.parse(fh, "genbank").next()
fh.close()

# Below here you type in the things I specify 
# you should look at later. The object you
# are testing them on are macaca

```

We are now going to explore this genbank file.

First, add `print gbk` at the bottom of the file, then save and run.

Question: can you figure out what the id of this sequence is?
Question: can you figure out which species this sequence is from?

Second, remove the line specified above, add `print gbk.id`, save and run.  
Third, remove the line specified above, add `print gbk.annotations`, save and run.  

Question: can you figure out what kind of thing you printed out? You should see something with curly brackets, with elements inside with colons inbetween. Hint: you used them quite extensively when working with translation tables.

Fourth, remove the line specified above, add `print gbk.annotations["organism"]`, save and run.  

### Add organism name to fasta description line

Our goal now is to create a script so that it can read a genbankk file, access the organism name and add it to the fasta description name, and then print this out in fasta format.  As you saw with the script above, you can do that by accessing the annotations of the genbank record.

#### Reading in files ####

We first need a genbank file to work with. Save this file as before [this one](mb.gbk) as mb.gbk

Next, save the following in a script file named name_with_organism.py

```Python
import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fh = open(sys.argv[1], "r")

for record in SeqIO.parse(fh, "genbank"):
    print(record.id)

fh.close()
```

Run it, (python name_with_organism.py mb.gbk) and you will see the ids of the sequences in the mb.gbk file printed on screen. 

Question: how many sequences are there in that gbk file?  

Try running it with the macaca file too.

#### Creating a new id ####

Now, can you remember how you could get at the organism of a sequence? Add a print statement that will print this out on the line after `print record.id`, so that you will first get one line with the id of the sequence, and one with the organism name.

As you can see, these are now just strings. Strings can be added together. 

In this case, we have two words in our string, the genus name and the species name. We will only use the species name.

Question: In a string with two words, what do you use to get at only the last word?  

We are now going to create a new id for each entry. This can be done by doing this:

```Python
   # Note: we are now inside the for loop
   organism = record.annotations['organism']
   species_name = organism.split()[1]
   record.id = species_name + "_" + record.id
```

Add a print statement inside the for loop after you have assigned a new value to record.id, so that you get to see what this is.


#### Writing out files ####

We are now going to write this out to file. We now need to also have an out file open. 

Look at this example and figure out which portions of this you need in your own script:

```Python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fh = open(sys.argv[1], "r")
fo = open(sys.argv[2], "w")

for record in SeqIO.parse(fh, "genbank"):
    SeqIO.write(record, fo, "fasta")
fh.close()
fo.close()

```

Congratulations, you have now created your own custom conversion script!
