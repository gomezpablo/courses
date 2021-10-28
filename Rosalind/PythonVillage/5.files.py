# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:43:22 2021
@author: pablo

Problem
Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

"""
# Packages
import os

# Set datasets working directory
os.chdir(r'C:\Users\pablo\Documents\formation\Rosalind\PythonVillage\datasets')

# Function
def even_numbered_lines(file, new_file):
    """This function is going to take an existing file and it is going to create
    a new file containing only the even lines of the origianl file"""
    
    line_counter = 0
    
    with open(file, 'r') as infile, open(new_file, 'a') as outfile:
        for line in infile:
            line_counter = line_counter + 1
            if line_counter % 2 == 0:
                outfile.write(line)
            
# Test
file = 'rosalind_ini5.txt'
new_file = 'rosalind_ini5_even_lines.txt'
even_numbered_lines(file, new_file)
