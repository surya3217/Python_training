"""
Name: Temperature Calculator         
Problem Statement:
    Assume today's temperature in Jaipur is 29 degree Centigrade. 
    Calculate the temperate in Degree Fahrenheit and print it.
    Calculate the temperature in Degree Kelvin and print it.
"""

temp= float(input('Enter the temperatute of city in degree Centigrade: '))
print('Temperate in Degree Fahrenheit: ',(temp*9)/5 +32,chr(176),'F',sep='')
print('Temperature in Degree Kelvin: ',temp+273,'K')
