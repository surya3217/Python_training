# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:56:56 2020

@author: Windows10
"""

"""
Name: 
    Height Calculator         
Filename:
    height_cal.py
Problem Statement:
    Lets assume your height is 5 Foot and 11 inches 
    Convert 5 Foot into meters and 
    Convert 11 inch into meters and 
    print your total height in meters and 
    print your total heigjt in centimetres also
Data:
    Not required
Extension:
    Take the height of the user from input 
Hint: 
    1 Foot = 0.3048 meters 
    1 inch = 0.0254 meters 
    1 m = 100 cm
    """
foot= float(input('enter your height in foot: '))
inch= float(input('enter your height in inches: '))
meter= (foot*0.3048)+(inch*0.0254)
print('Height in meters: ',meter,'m')
print('Height in centimetres: ',meter*100,'cm' )