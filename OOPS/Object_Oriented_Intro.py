# OOP's in Python 
"""
Introducing the keywords of OOP

Prodecudral ( Data and Function as seperate entities)

State and Behaviour
Attributes and Methods
Characteristics and Functionality


Logically group data and function 
Easy to re use and build upon
Data and function are known as attributes( characteristics ) 
and methods ( function associated with a class )
class is a blueprint for creating instances (objects)


Introduce the concept of Radio Blueprint 

 
Classes and Instances

Represent Employee in Python 
Individual employee will have specific attributes and methods
Name
email address
Pay


class is a blueprint for creating instances 
each individual employee would be the instance of the class 
"""


class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()


print ( emp_1)
print ( id(emp_1))

print ( emp_2)
print ( id(emp_2))


# Why should you set the instance variable manually everytime
# It should have been set when we create the instance (object)
# Use __init__ method to create the instance variables ( constructor )
# create init method within the class 
# self syntax is how Python tells a method “make use of all
# the previously defined attributes and methods in this instance.”
# However, you never type self when you call the method.
# The init method. is called whenever you create an instance of the class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"
		# declaring simple variables within this method will have limited scope

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

print(emp_1.email)
print(emp_2.email)


# Adding Action (Methods) to the class using functions 
# Display Full Name of the employee 
# create method in the class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last) 

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

print ( emp_1.fullname() )
print ( emp_2.fullname() )

# calling the methods from the class name, 
# but we need to pass the instance
# thats why the self object is passed

print (Employee.fullname(emp_1))
print (Employee.fullname(emp_2))



# class variable that holds the number of employees depending on the instances created 

class Employee:
    # declare this in the class level 
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"
        # we need to increase the value in the init method
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first,self.last) 


emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)


print ( Employee.num_of_emps )



# Inheritance - Creating Subclasses

class Developer( Employee ) :
    pass

issubclass(Developer,Employee)

dev_1 = Employee ("Sylvester", "Fernandes",50000)
dev_2 = Employee ("Yogendra", "Singh",60000)

print (dev_1.email)
print (dev_2.email)

dev_1 = Developer ("Sylvester", "Fernandes",50000)
dev_2 = Developer ("Yogendra", "Singh",60000)

print ( dev_1.email )
print ( dev_2.email )

# This gives a clear picture of the inheritance and the variables 
# Method resolution order
print ( help( Developer ) ) 


