# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 12:11:32 2020

@author: Windows10
"""

"""
Name: 
    Adult Body Mass Index Calculator         
Filename:
    bmi_cal.py
Problem Statement:
    Assuming your weight in kilogram and height in meters  
    Calculate your BMI value and print it ?
Data:
    Not required
Extension:
    Take the height and weight of the user from input 
Hint: 
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI
    """
# weight =50 kg, height= 1.5 m, bmi= 22.2kg/m2
    
weight= float(input('enter weight in kg: '))
height= float(input('enter height in m: '))
bmi= (weight/height)/height
print("Body Mass Index: {:.4f}".format(bmi),'kg/m\u00b2')
