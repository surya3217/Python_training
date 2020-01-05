# -*- coding: utf-8 -*-
"""
Name: 
    Temperature Calculator         
Problem Statement:
    Assume today's temperature in Jaipur is 29 degree Centigrade. 
    Calculate the temperate in Degree Fahrenheit and print it.
    Calculate the temperature in Degree Kelvin and print it. 
Hint: 
    Multiply by 9/5 and add 32  to get in Fahrenheit
    Add 273 approximately to get in Kelvin
"""

temp= float(input('enter the temperatute of city in degree Centigrade: '))
print('temperate in Degree Fahrenheit: ',(temp*9)/5 +32,chr(176),'F',sep='')
print('temperature in Degree Kelvin: ',temp+273,'K')
