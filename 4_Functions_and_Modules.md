#Python 3 : Functions and Modules
-----------------------

A function is a block of code that performs a specific task. In this section we
will learn how to write our own functions and modules, and import them. The example used in this section is a simple one. But the main purpose of this part of the tutorial is not only to show you how to write our own functions and modules but also why do it. The goal is to show you how and why modularisation of the source code is a good programming practice.

##Writing our own functions

So far we have used the python interactive Python shell and also written Python scripts (typing up the source code in a file and then running it in IDLE). We will now show how to "package" this source code into functions. This will allow us to reuse the same code easily multiple times (without having to run it each time manually). 

NOTE: you are supposed to fill in some code in each function. You should have most of this from exercises done previously.

Put the following code in a script file named dna_functions.py

```python
def get_atcontent(dna_string):
   # Write the code that would
   # be necessary to calculate
   # the at content of a DNA string
   # Return the at content

def get_sequence(lines):
   # Write the code necessary to
   # get a dna string from a fasta
   # formatted sequence file
   # Input is a fsa file read into
   # a list with one line per element
   # in the list. Remember: each line
   # ends in a newline!
   # Return the dna string


fh = open("hbb.fsa", "r")
readlines = fh.readlines()
fh.close()

sequence = get_sequence(readlines)
at_content = get_atcontent(sequence)

print "The AT content is", at_content
```

The keyword for defining a function is *def*. After that we have the function name followed by any arguments in parenthesis. After that comes the code that the function performs. Input to the function is available in the arguments passed to it.

NOTE: any variables defined in the function is not available outside of it. Any results that is created in it must be returned to the outside using the return statement.

Run the script. What is the AT content of the string?
NOTE: the file hbb.fsa has to be in the same directory as the script.


##Creating modules

In the same file, after the functions, add the following:

```python

if __name__ == "__main__":
```
Move the rest of the code, from opening the input file and so on, after this if statement. Note: you need to indent it properly!

Now run this script just like it is. You should get the same results as before.

But, how come this code is run?  What happens is that when you run a script directly from the command line, a variable that is called "\_\_name\_\_" is set to have the value "\_\_main\_\_" then ask python
to test on this variable with an if statement, and if it is true, whatever is inside of it is run. In this case, we test the function. 

This variable will not be set to "\_\_name\_\_" if we use this script inside of another script.

We are now going to import these functions into a different script. Note, when we do `import modulename`, we have to prepend the function with the module name, like this: modulename.functionname.


```python
import dna_functions

fh = open("hbb.fsa", "r")
lines = fh.readlines()
fh.close()

##Now, using the lines above as input, do the following:

# 1. get the sequence as a string
# 2. calculate the AT content, and print it

```

What happens here is that Python goes into the dna_functions file and gets the functions that we specified, and uses that inside of this script. We get at the function by using the import statement. 


** Optional homework**

Look at the translation script you created last week, and fill in the following functions:


```python

def read_fasta(lines):
    # Input: readlines on a filehandle input
    # Return a string containing the fasta
    # sequence found in the file
    
def read_translationtable(lines):
    # Input: readlines on a filehandle input
    # This file contains codon-aminoacid paris
    # Create a dictionary where the codon is
    # the key, and the aminoacid is the value
    # return the dictionary
    
def translate(sequence, translationtable):
    # sequence is a dna string, translationtable
    # is a dictionary where codons are the key
    # and the aminoacids are the values.
    # Iterate over the string, get codons, and
    # translate to protein. 
    # return the protein string
    
def create_fasta_string(header, sequence):
    # header is a fasta header with a >
    # sequence is a string that we want
    # to print, 60 characters to a line
    # Create a fasta outut formatted string
    # return string
    
if __name__ == "__main__":
   fh = open("hbb.fsa", "r")
   fastalines = fh.readlines()
   fh.close()
   header = fastalines[:1]
   sequence = read_fasta(lines)

   fh = open("translationtable.txt","r")
   tablelines = fh.readlines()
   fh.close()
   translationtable = read_translationtable(tablelines)

   protein = translate(sequence, translationtable)
   fastastring = create_fasta_string(header, protein)

   fo = open("hbb_proteins.fsa", "w")
   fo.write(fastastring)
   fo.close()

```
