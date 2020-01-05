# -*- coding: utf-8 -*-
"""
Name: 
    Target Heart Rate Calculator         
Problem Statement:
    Calculate the Maximum Heart Rate and Target Heart Rate Range 
    ( Lower and Higher value ) of a person of a specific age.
    Lets Assume your age is 21 years
Hint: 
    Subtract your age from 220 to get your Maximum Heart Rate
    Lower end of your Target Heart Rate is 70% of Maximum Heart Rate
    Higher end of your Target Heart Rate is 85% of Maximum Heart Rate
    Heart Rate = Beats per minute
    """

age= int(input('enter age: '))
max_hrt= 220- age
low_end= (max_hrt*70)/100
high_end= (max_hrt*85)/100
print('Maximum Heart Rate: ',max_hrt)
print('Target Heart Rate Range: ({},{})'.format(low_end,high_end))

    