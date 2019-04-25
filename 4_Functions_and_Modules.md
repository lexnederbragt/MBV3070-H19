# Python 4: Functions and Modules
-----------------------

A function is a block of code that performs a specific task. In this section we
will learn how to write our own functions and modules, and import them. The main purpose of this part of the tutorial is to show you how to write our own functions and modules and hopefully also why you should do it. The goal is to show you how and why modularisation of the source code is a good programming practice.

## Writing our own functions

So far we have used Jupyter notebooks to write Python code. We will now show how to "package" this source code into functions. This will allow us to reuse the same code easily multiple times (without having to type it in each time). You can then also import your funtions in other programs. Finally, we will also practice running Python by creating script files and having these executed on the command line.

When modularising code, first, you will create module script file. You will then use this script as a script itself. Second, you will create a new script, where you import and use the script you just created.

The keyword for defining a function is *def*. After that we have the function name followed by any arguments in parenthesis. After that comes the code that the function performs. Input to the function is available in the arguments passed to it.

The code below can be found in a script file named `translate_module.py`. You are supposed to fill in some of the code for each function. Hint: you should have most of this code from exercises done previously.

NOTE: any variables defined in the function are not available outside of it. Any results that is created in it must be returned to the outside using the `return` statement.

Run the script, using `hbb.fna` you created in `3_Reading_and_Writing_files` as the fasta dna input file, `translationtable.txt` as the translation table input file, and then name the output what you feel like. The output file should not already exist in the directory that you are in, but the input file should.


```Python
import sys

def read_fasta(lines):
    # Input: a list containing the lines found
    # in the file, i.e. the results from
    # fh.readlines() in Part 1
    # Return a string containing the fasta
    # sequence found in the file

def read_translationtable(lines):
    # Input: the result from fh.readlines()
    # from Part 2
    # This file contains codon-amino acid pairs
    # Create a dictionary where the codon is
    # the key, and the amino acid is the value
    # Return the dictionary

def translate(sequence, codon_table):
    # sequence is a dna string, codon_table
    # is a dictionary where codons are the key
    # and the amino acids are the values.
    # Do a for loop over the sequence, get codons,
    # and translate to protein using the dictionary.
    # Return the protein string.

def create_fasta_string(header, sequence):
    # header is a fasta header with a >,
    # sequence is a string that we want
    # to print, 60 characters to a line
    # Create a fasta output formatted string
    # using a for loop, and return the results.
    # Remember, you also need the header line,
    # so first assign the text in the header variable
    # to the variable that will contain the output,
    # and keep adding the rest of the string to it,
    # 60 characters at a time.

if __name__ == "__main__":
    # Part 1: here we open the first file given
    # on the command line. This file contains our
    # fasta sequence to be translated.
    # First we open the file,
    fh = open(sys.argv[1], "r")
    # We read the contents into a list
    fastalines = fh.readlines()
    # We close the file
    fh.close()
    # We store the first line, to have the
    # fasta header stored
    header = fastalines[0]
    # And we use the read_fasta function to
    # convert the contents of the file into
    # one long string
    sequence = read_fasta(fastalines)

    # Part 2: Here we read in a translation table,
    # and make a dictionary out of it.
    # First we open the second file given on the
    # command line
    fh = open(sys.argv[2],"r")
    # We read the contents into a list
    tablelines = fh.readlines()
    # We close the file
    fh.close()
    # And use the function read_translationtable to
    # process the file contents to get a dictionary
    # of codons and amino acids back.
    codon_table = read_translationtable(tablelines)

    # Part 3. Here, we use the dna sequence we got
    # from the dna file, and the translation table
    # in the function translate to translate the
    # dna into protein
    protein = translate(sequence, codon_table)
    # Here, we use the header we saved above, with the
    # protein string in the method create_fasta_string
    # to create nice output which we can save to a file.
    fastastring = create_fasta_string(header, protein)

    # Part 4: here, we get a file name from the
    # command line, open it, and save our string
    # to it
    # Here, we open the file.
    fo = open(sys.argv[3], "w")
    # Here, we write the string to the file
    fo.write(fastastring)
    # Then we close the file
    fo.close()

```

## Using it as a module

Towards the end of the file, we have the following line: "if __name__ == "__main__":". This if statement is only true if you are running this script. If you use code from this script elsewhere, it is not true. What happens is that when you run a script directly from the command line, a variable that is called `__name__` is set to have the text string `__main__` as value.  We then ask python to test on this variable with an if statement. If the value of the variable `__name__` is `__main__`, then the if statement is true and whatever is inside of it is run. This variable will not be set to `__name__` if we use this script inside of another script using an import statement.

We are now going to import these functions into a different script - call this `translate_usemodule.py`. Note, when we do `import modulename`, we have to prepend the function with the module name, like this: `modulename.functionname`.


```Python
import sys
import translate_module
fh = open(sys.argv[1], "r")
fastalines = fh.readlines()
fh.close()

# Now, using the lines above as input, do the following:

header = fastalines[0]
sequence = translate_module.read_fasta(fastalines)
fastastring = translate_module.create_fasta_string(header, sequence)
print(fastastring)

fo = open(sys.argv[2], "w")
fo.write(fastastring)
fo.close()

```
This script takes a fasta file, and does formatting on it. Not incredibly useful, but it does show that you can use code that is not in the script you wrote, but in another file, which then is a python module.

What happens here is that Python goes into the `translate_module` file and gets the functions that we specified, and uses that inside of this script. We get at the function by using the `import` statement.

Try running it, using the `hbb.fna` file as input.
