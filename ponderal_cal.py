# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 12:47:15 2020

@author: Windows10
"""

"""
Name: 
    Ponderal Index Calculator         
Filename:
    ponderal_cal.py
Problem Statement:
    Calculate the Ponderal Index of a Person and print it
Data:
    Not required
Extension:
    Take the height and weight of the user from input 
Hint: 
    Divide the BMI by your Height ( meters ) to get your Ponderal Index
  """
  
weight= float(input('enter weight in kg: '))
height= float(input('enter height in m: '))
bmi= (weight/height)/height
pond= bmi/height
print("Body Mass Index: {:.3f}".format(bmi),'kg/m\u00b2')
print("Ponderal Index: {:.3f}".format(pond),'kg/m\u00b3') 
    