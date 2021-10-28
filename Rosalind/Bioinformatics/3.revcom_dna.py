# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:56:28 2021
@author: pablo

Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the 
symbols of s, then taking the complement of each symbol (e.g., the reverse complement 
of "GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.

"""

# Function
def rev_complement(s):
    """This function is going to take a DNA sequence and it is going to return
    the reverse complementary"""
    
    revcom_seq = ""
    
    for nt in s[::-1]: # for each nucleotide in the reverse sequence
        
        # get complementary
        if  nt == "A":
            revcom_seq += "T"
        if  nt == "T":
            revcom_seq += "A"
        if  nt == "G":
            revcom_seq += "C"
        if  nt == "C":
            revcom_seq += "G"
    
    return print(revcom_seq)
            
       
    

# Test
s = "GGGGATCAGCAGAATACACAAATGGACGCCGGGCGGTTTCCTGAGATAAGAGAGAGTAAAACTCACAACTATCGTCTCCACTCTGTAAGTCGCTAACTCGATCCCACGGGTCCATCGCACTCGTGTACTTCACCCGAGTGAAAGGAGGAACTATGCTGTGCTTCCGGGAAGTGCCTGAGGTAAAAGGTCAGGCCATAACAATATCCGAACTATCACCGGCAAGCTCGGACAGTTGCACGCCGATACATAGTAAGGGACGTGAACGGCCGATCACTCGCCTCTTGTAGAGGTTGGTAGGCCGTATAGTTAACGTGATTTCTTTGACGATAGTAAATCTGTCATGGTGGGTAAAGCTTGTATAGATATCGGGACCCAGTATTTCTTGTATTCCGTCATGTATACGTTGCCTACTAGGGGATCCGCAAACCTTACAAAGACGTATCCCTATGTCTCGCTCCGGGCACAACCTACCCAATCCCATGAGACCGCCCACTAAAACGATTCGAAGGTCACTTACAGTAATGCGGAGTGACAACTGGACTCCACGAAATGAAACCGTCCGGGGTAGAGGCCAGCGCCCAAGACACTGATCATGAAGCCTCAGCGCACCGGGGTTGACGCTACTCGTTCAAGAAAACCTTTTACATTCGCAACCTTCCGGGGTCGTCTTTGCAGGAGACGAACCTTGTTACAACTACGCCGCATGTCAAGTGATGTGTGTGTTTAAAGGGGGGTGAGTCTGCATAAGTTCAACGCATAAGTGTGTTCACCCACTGCGACTGAAGTGACGCTCACCTTACCTTTGACACACCATATTGTTATACTTCGAGAGGCTCGTCGGGTCGCCCCTTCTCACCAATCAGAATCTCGAGCAGGACGGTGTGCCATAGTATGGAGATTCGCGCGTA"
rev_complement(s)