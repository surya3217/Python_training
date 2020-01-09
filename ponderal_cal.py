"""
Name: 
    Ponderal Index Calculator         
Problem Statement:
    Calculate the Ponderal Index of a Person and print it
Extension:
    Take the height and weight of the user from input 
Hint: 
    Divide the BMI by your Height ( meters ) to get your Ponderal Index
"""
  
weight= float(input('Enter weight in kg: '))
height= float(input('Enter height in m: '))
bmi= (weight/height)/height
pond= bmi/height
print("Body Mass Index: {:.3f}".format(bmi),'kg/m\u00b2')
print("Ponderal Index: {:.3f}".format(pond),'kg/m\u00b3')
    