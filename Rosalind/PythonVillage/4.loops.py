# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:32:17 2021
@author: pablo

Problem
Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
"""
# Function
def odd_int_summatory(a,b):
    
    """This function is going to sum all the odd integers between the 2 values
    given"""
    
    total = 0
    
    for i in range(a,b+1): # include last int of the interval 
        
        if i % 2 != 0: # if number is odd (remainder after div by 2 is not 0), include in the summatory 
            
            total = total + i
    
    return total

# Test
odd_int_summatory(4039,8927)