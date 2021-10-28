# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:24:17 2021
@author: pablo

The GC-content of a DNA string is given by the percentage of symbols in the 
string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. 
Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. 
A commonly used method of string labeling is called FASTA format. In this format, 
the string is introduced by a line that begins with '>', followed by some labeling
 information. Subsequent lines contain the string itself; the first line to begin
 with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the 
ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.


Problem
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the 
GC-content of that string. Rosalind allows for a default error of 0.001 in all 
decimal answers unless otherwise stated; please see the note on absolute error below.
"""

import os
os.chdir('C:\\Users\\pablo\\Documents\\formation\\Rosalind\\Bioinformatics\\datasets')


# Function
def gc_content(fasta):
    """This function is going to return the GC content of the sequence with the
    highest C content, in the format of sequence id, new line and %GC"""
    
    ID_vector = [] # empty list to contain all sequences ID
    GC_vector = [] # empty list to contain GC content
    
    with open(fasta, 'r') as infile:
       
       G_total = 0
       C_total = 0
       N_total = 0
       GC_content = 0
       
       for line in infile:
            line = line.rstrip() # remove \n character at the end of each line
            
            if line[0] == ">":   # get sequence ID
                
                if GC_content != 0:
                    GC_vector.append(GC_content) # add GC content to vector because all the nt lines have been computed
                
                ID_vector.append(line[1:])
                
                GC_content = 0
                G_total = 0
                C_total = 0
                N_total = 0
            
            
            
            elif line[0] == "A" or "T" or "C" or "G": # compute GC content of the DNA sequence
                G_total = G_total + line.count("G")
                C_total = C_total + line.count("C")
                N_total = N_total + len(line)
                GC_content = 100*(G_total + C_total)/N_total
        
    GC_vector.append(GC_content) # add GC content to vector of last sequence
    
    # return sequence ID and GC content of the sequence with the highest GC content
    print(ID_vector[GC_vector.index(max(GC_vector))])
    print(max(GC_vector))
            
            
            

# Test
fasta = '4.3.rosalind_gc.txt'
gc_content(fasta)