# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:46:00 2021
@author: pablo

Problem
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d 
(with space in between), inclusively. In other words, we should include elements 
s[b] and s[d] in our slice.

"""
# Function
def string_slicer(string, a, b, c, d):
    
    """This function is going to slice a given string from the first index to the
    second (included) and the third index to the fourth (included)
    """
    
    return print(string[a:b+1] + " " + string[c:d+1])

# Test
s = "xnYPejp134MLUqqpf4dpbCakNR1ggdSAbXFuVrBoUFfXi0SQAWpQ7sXisjwG8SXB9tflB2KaqFgljOrdMZ040BradypterusQLfbx4KfyHPQthaVgmlB4bfpnippon8w4gwZZCKQGoSknR8WyuE0962MN6BjeyVXyqbmL4XvVikK0R."
a = 85
b = 95
c = 120
d = 125

string_slicer(s,a,b,c,d)    