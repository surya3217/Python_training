"""
Name: 
    Adult Body Mass Index Calculator         
Problem Statement:
    Assuming your weight in kilogram and height in meters, Calculate your BMI value and print it?
Extension:
    Take the height and weight of the user from input 
Hint: 
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI
    """
# weight =50 kg, height= 1.5 m, bmi= 22.2kg/m2
    
weight= float(input('Enter weight in kg: '))
height= float(input('Enter height in m: '))
bmi= (weight/height)/height
print("Body Mass Index: {:.4f}".format(bmi),'kg/m\u00b2')

'''Output:
enter weight in kg: 50
enter height in m: 1.5
Body Mass Index: 22.2222 kg/m²'''