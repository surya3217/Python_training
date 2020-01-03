# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:22:56 2020

@author: Windows10
"""
"""
Name: 
    Age Calculator         
Filename:
    age_cal.py
Problem Statement:
    Lets assume your present age is 21 today
    What would be your age after 5 years from today 
    How old were you 10 years back
Data:
    Not required
Extension:
    Take the present age of the user from input 
Hint: 
    You need to add 5 to present age to calculate future age 
    You need to subtract 10 present age to calculate your past age
    """

cur_age= int(input("Enter current age: "))
print('Age after 5 years:',cur_age + 5)

print('10 years back age:',cur_age -10)
