"""
Code Challenge
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]
"""

lis1= [7, 13, 17, 231, 12, 8, 3]

def compute():
    num= 0
    while num < len(lis1):
        yield lis1[num]
        num += 1 


avg= compute()
suml= 0
print('Running Average:\n')
for ind,x in enumerate(avg,1):    
    suml+= x
    print( float(suml/ind) )

##########################################################################

""" Example of Primes """

def check_prime(number):    
    for divisor in range(2, int(number ** 0.5) + 1):        
        if number % divisor == 0:            
            return False    
        return True

def Primes(max):    
    number = 1    
    while number < max:        
        number += 1        
        if check_prime(number):            
            yield number

## start
primes = Primes(10)

next(primes)
next(primes)
next(primes)
#next(primes)
primes = Primes(10)

#####################################################################

"""Example of Counting"""
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

myCountDown = countdown(10)

type(myCountDown)

next(myCountDown)
next(myCountDown)
next(myCountDown)



