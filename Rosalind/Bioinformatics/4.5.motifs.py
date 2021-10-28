# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:35:20 2021
@author: pablo

Problem
Given two strings s and t, t is a substring of s if t is contained as a contiguous 
collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its 
left, including itself (e.g., the positions of all occurrences of 'U' in 
"AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
 of s is denoted by s[i].
 
 A substring of s can be represented as s[j:k], where j and k represent the starting 
 and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", 
 then s[2:5] = "UGCU".
 
 The location of a substring s[j:k] is its beginning position j; note that t will 
 have multiple locations in s if it occurs more than once as a substring of s 
 (see the Sample below).
 
 Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
 """

# Function
def find_motifs(sequence, motif):
    """This function is going to return the initial index (1-based) of all motifs
    found in a sequence"""
    
    if len(motif) >= len(sequence): # check motif is not longer than the sequence
        print("Error: motif cann't have the same or longer lenght than the sequence")
    
    else: # find motifs
        motifs_index = []
        start = 0 # define initial index
        
        for nt in sequence: # parse the sequence to find motifs
            
            if nt == motif[0]:    
                end = start + len(motif) # define end index 
                
                if sequence[start:end] == motif: # check if sequence contains motif
                    motifs_index.append(start+1) # python indexes are 0 based, correct that to return a 1-based index
            start = start + 1 # update index
        
        return print(*motifs_index, sep = " ")


        
# Test
s = "TAAGCTGAGATATGAGATAGTGAGATAATGAGATAGATGAGATAATGAGATACTTGAGATATGAGATATGAGATATGAGATACGGTCCCTGAGATATCTGAGATATGAGATATGTGAGATAGGTGAGATATGAGATATGAGATAACTGAGATAAGGGCCTGAGATAGTTGAGATAAAATGAGATACCGATGCTGAGATATGAGATAGAAACCTGAGATACAATGAGATATTCTCATCTAGCATTGAGATACTGAGATAGGAAATAATGGCTGAGATAACATTCTCCTGAGATAATTTTGAGATAGTGAGATATGAGATATGAGATACTGAGATATGAGATATGCCGCGAGTTTGAGATAGAACTGAGATATGAGATAGTGAGATATACTGAGATACGGAGCGGATGAGATACTCATATGAGATAGATCAGCTCAGACGACTGAGATAGCCTTGGATGAGATATGAGATAGTAATGAGATATTGAGATACGAGAGTTGAGATAGTCCGACGCGCTGAGATAGATGAGATATGCTTTCTTACCCCTGAGATAATAAGTGAGATACCTGAGATAGTGAGATATGAGATAGGGGTTTTCATTTGATTGAGATATGAGATATGAGATAATTGAGATAAGAGTTTGAGATACGCTATCTGAGATAAAAGCCTGAGATAATTTGAGATATTGAGATAGATGAGATACTGAGATAGCTAAGGCCCATTGAGATATTGAGATACCTACGTCCATGAGATAATATGAGATAGTGAGATACCCTGAGATAAATCAAGATGAGATAACTCTGAGATAATGAGATATGAGATATAATGAGATAATGAGATACCGTTCTGAGATAATGAGATATTACTGAGATACTGAGATACGATTGAGATAAATGTGAGATAAATTGAGATAAGAATGAGATATACTGAGATACACTGAGATA"
t = "TGAGATATG"

find_motifs(s,t)
