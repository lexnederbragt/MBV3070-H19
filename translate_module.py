join_lines(import sys

def join_lines(lines):
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
    # convert the remaining contents
    # of the file into one long string
    sequence = join_lines(fastalines[1:])

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
