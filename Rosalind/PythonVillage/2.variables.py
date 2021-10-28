# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:32:50 2021
@author: pablo

Problem
Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right 
triangle whose legs have lengths a and b.

"""
# Function
def calculate_square_hypotenuse(a,b):
    
    """This function is going to take 2 integers and it is going to return the square 
    hypotenuse of the triangle whose legs have the lengths of these 2 integers"""
    
    c = a**2 + b**2
    
    return c
 
# Test    
calculate_square_hypotenuse(924,862)