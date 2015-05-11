#Python 3 : Functions and Modules
-----------------------

A function is a block of code that performs a specific task. In this section we
will learn how to write our own functions and modules, and import them. The main purpose of this part of the tutorial is to show you how to write our own functions and modules and hopefullyy also why do it. The goal is to show you how and why modularisation of the source code is a good programming practice.

##Writing our own functions

So far we have used the python interactive Python shell and also written Python scripts (typing up the source code in a file and then running it with python). We will now show how to "package" this source code into functions. This will allow us to reuse the same code easily multiple times (without having to run it each time manually). First, you will create the module. You will then use this script in itself. Second, you will create a new script, where you import and use the script you just created.

NOTE: you are supposed to fill in some code in each function. Hint: you should have most of this code from exercises done previously.

Put the following code in a script file named translate_module.py

```python
def read_fasta(lines):
    # Input: 
    # Return a string containing the fasta
    # sequence found in the file
    
def read_translationtable(lines):
    # Input: the result from filehandle readlines().
    # This file contains codon-amino acid pairs
    # Create a dictionary where the codon is
    # the key, and the amino acid is the value
    # Return the dictionary
    
def translate(sequence, translationtable):
    # sequence is a dna string, translationtable
    # is a dictionary where codons are the key
    # and the amino acids are the values.
    # Do a for loop over the sequence, get codons,
    # and translate to protein using the dictionary.
    # Return the protein string.
    
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
   sequence = read_fasta(fastalines)

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
The keyword for defining a function is *def*. After that we have the function name followed by any arguments in parenthesis. After that comes the code that the function performs. Input to the function is available in the arguments passed to it.

NOTE: any variables defined in the function is not available outside of it. Any results that is created in it must be returned to the outside using the return statement.

Run the script. What is the protein that the file codes for?
NOTE: the file hbb.fsa has to be in the same directory as the script.


## Using it as a modules

Towards the end of the file, we have the following line: "if __name__ == "__main__":". This if statement is only true if you are running this script. If you use code from this script elsewhere, it is not true. What happens is that when you run a script directly from the command line, a variable that is called \_\_name\_\_ is set to have the text string "\_\_main\_\_" as value.  We then ask python to test on this variable with an if statement. If the value of the variable \_\_name\_\_ is "\_\_main\_\_", then the if statement is true and whatever is inside of it is run. This variable will not be set to "\_\_name\_\_" if we use this script inside of another script using an import statement.

We are now going to import these functions into a different script - call this translate_usemodule.py. Note, when we do `import modulename`, we have to prepend the function with the module name, like this: modulename.functionname.


```python
import translate_module
fh = open("hbb.fsa", "r")
fastalines = fh.readlines()
fh.close()

##Now, using the lines above as input, do the following:

header = fastalines[0]
sequence = translate_module.read_fasta(fastalines)
fastastring = translate_module.create_fasta_string(header, sequence)
print fastastring

fo = open("hbb_proteins.fsa", "w") 
fo.write(fastastring)
fo.close()

```
This script basically takes a fasta file, and does formatting on it. Not incredibly useful, but it does show that you can use code that is not in the script you wrote, but in another file, which then is a python module.

What happens here is that Python goes into the translate_module file and gets the functions that we specified, and uses that inside of this script. We get at the function by using the import statement. 


## Using the sys module.

So far, you have hardcoded the file name into each script file. Wouldn't it be nice to be able to just add the filename on the command line, so that you don't have to change the script every time you want to run it? And, wouldn't it be nice if you could specify the output file name also?

In the translate_usemodule.py script do the following:

1. include the line 'import sys' on top of the file (leave the ' out).
2. replace "hbb.fsa" with 'sys.argv[1]' (leave the ' out).
3. replace "hbb_proteins.fsa" with 'sys.argv[2]' (leave the ' out).

Now, try running this on the command line:

```
python translate_usemodule.py hbb.fsa hbb_out.fsa
```

As you see, you have now specified the input and the output file on the command line - you can now use a different input file, and also save the results under a different output file name.

Try running it again, but now use your own personal name instead of hbb_out. Have a look at the file. Does it look the same?
