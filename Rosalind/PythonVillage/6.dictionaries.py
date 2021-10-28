# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:03:25 2021
@author: pablo

Problem
Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated 
by spaces. Words are case-sensitive, and the lines in the output can be in any order.

"""
# Function
def string_n_occurrences(string):
    """Create a list with each element of the string and a list containing only
    uniq elements, print each uniq element with the number of times it appears
    in the list"""
    ls = string.split()
    ls_uniq = set(ls)
    for element in ls_uniq:
        number_times = ls.count(element)
        print(element, number_times)

# Test
string = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
string_n_occurrences(string)