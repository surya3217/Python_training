# create a file prime.py 

'''
1. First make a function for the problem
2. then import unittest library
3. Make your test class and inherit unitTest.TestCase class in our test class
4. then write all the possible test cases usinf assert statment
5. then call its main function and the test cases will run
6. for test cases which follow condition, passed
7. for test cases which does not follow condition, failed 
'''

import math
def is_prime(n):
  """Determine if a non-negative integer is prime"""
  if n < 2 :
    return False

  # OFF BY ONE Error, solution is to add +1  
  # for i in range (2, int(math.sqrt(n)) + 1 ):
  for i in range (2, int(math.sqrt(n)) + 1):
    if n % i == 0 :
      return False
  return True


# list of prime numbers

# is_prime WILL return TRUE  
# 2, 3, 5, 7, 11, 13, 17, 19, 23
  
# is_prime WILL return FALSE  
# 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28

is_prime(1)   # SUCCESS
is_prime(2)   # SUCCESS
is_prime(4)   # FAIL
is_prime(8)   # FAIL   
is_prime(11)  # SUCCESS
is_prime(25)  # FAIL 
is_prime(28)  # SUCCESS
  

"""
Sequence of Demo for testing

prime.py
test0.py
test1.py
"""

# test0.py
from prime import is_prime

def test_prime(n,expected):
  if is_prime(n) != expected :
    print(f"ERROR on is_prime{n}, expected {expected}")
  else:
    print("PASSED")
    
"""    
test_prime(1,False)
test_prime(2,True)
test_prime(8,False)
test_prime(11,True)
test_prime(25,False)
test_prime(28,False)
"""

# test1.py
import unittest

from prime import is_prime

class Tests ( unittest.TestCase):
  def test_1(self):
    """Check that 1 is not prime. """
    self.assertFalse(is_prime(1))

  def test_2(self):
    """Check that 2 is prime. """
    self.assertTrue(is_prime(2))

  def test_8(self):
    """Check that 8 is not prime. """
    self.assertFalse(is_prime(8))

  def test_11(self):
    """Check that 11 is prime. """
    self.assertTrue(is_prime(11))

  def test_25(self):
    """Check that 25 is not prime. """
    self.assertFalse(is_prime(25))

  def test_28(self):
    """Check that 28 is not prime. """
    self.assertFalse(is_prime(28))


if __name__ == "__main__":
  unittest.main()

 
# How to run the test from command line
# python prime.py
# python -m unittest test1.py
# or
# python test1.py 
# this should call the __main__ function of the code 
  
# Other Unit Test Methods 
  
# docs.python.org/3/library/unittest.html#unitTest.TestCase.debug
# Class needs to be inherited from TestCase class and the method to be defined starting with test_

"""
assertEquals(a,b)
assertNotEquals(a,b)
assertTrue(x)
assertFalse(x)
assertIs(a,b)
assertIsNot(a,b)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a,b)
assertNotIn(a,b)
assertIsInstance(a,b)
assertNotIsInstance(a,b)
"""
