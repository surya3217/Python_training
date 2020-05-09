"""
DICT COMPREHENSION
"""

"""
Dictionary comprehension takes in a group of values, performs some kind of task 
on them, and returns the result as a Dictionary.

{resulting_keys: resulting_values for iteration in series}
The input for a dictionary comprehension does not have to be a dictionary

Dictionary comprehension is a powerful concept and can be used to substitute 
for loops and lambda functions.
"""

"""dict comprehension to create dict with numbers as values"""
# {key:value for i in list}

new_dict={str(i):i for i in [1,2,3,4,5]}
print(new_dict)


"""Converting a dictionary from a list"""
words = ['car', 'house', 'plant', 'fisherman', 'picnic', 'rodeo']

# Write a code using simple for loop
word_dict=dict()

for word in words:
    word_dict[word] = len(word)    

print(word_dict)


"""Write a code using Dict Comprehension"""
word_dict = {word: len(word) for word in words}
print(word_dict)


""" skip this

# Only changing the value of the dictionary 
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
new_dict = {key: value * 2 for key, value in my_dict.items()}
print(new_dict)


# Changing the key and value of the dictionary 
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
new_dict = {key.upper(): value * 2 for key, value in my_dict.items()}
print(new_dict)


# Conditionals Within Dictionary Comprehensions
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

new_dict = {key: val for key, val in my_dict.items() if val > 2}
print(new_dict)

# With multiple if
new_dict = {key: val for key, val in my_dict.items() if val > 2 if key != 'd'}
print(new_dict)


#the syntax gets switched around once else is involved
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

new_dict = {(key.upper() if val > 2 else key): (val + 10 if val > 3 else val + 20) for key, val in my_dict.items()}
print(new_dict)


#Nested Dictionary Comprehensions
my_dict = {
    'A': {
        'a': 1,
        'b': 2,
        'c': 3},
    'B': {
        'd': 4,
        'e': 5,
        'f': 6}
}
    
new_dict = {outer_key: {inner_key: inner_val * 10 for inner_key, inner_val in outer_val.items()} for outer_key, outer_val in my_dict.items()}
print(new_dict)
"""

"""
Code Challenge

Consider the following problem, where you want to create a new dictionary 
where the key is a number divisible by 2 in a range of 0-10 and 
it's value is the square of the number. 

First write the solution using for loop and then rewrite using Comprehension
"""


"""
Code Challenges
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Let's suppose you need to create a new dictionary from a given dictionary 
but with items that are greater than 2

In the problem above, what if you have to not only get the items greater than 2 
but also need to check if they are multiples of 2 at the same time. 
"""

"""
Code Challenge
Use a dictionary comprehension to count the length of each word in a sentence.
"""

"""
Code Challenge

For all the numbers 1-1000, use a nested list/dictionary comprehension to find 
the highest single digit any of the numbers is divisible by 3
"""

"""
Code Challenge

Word Frequency COunter
www.google.com

Create a program using the Dict Comprehension
"""
#########################################################


"""
GENERATORS
"""

"""
Generators in Python look like functions which returns iterator object
Generator functions allow you to declare a function that behaves like an iterator.
An iterator is an object that can be iterated (looped) upon. 

The yield statement turns a functions into a generator.
A generator is a function which returns a generator object.
This generator object can be seen like a function which produces a sequence of 
results instead of a single object. 
The execution of the code stops when a yield statement has been reached.
"""

# Iterable
# Iterating over a list
ez_list = [1, 2, 3]
for i in ez_list:
    print(i)
    

# Iterating over a string
ez_string = "Generators"
for s in ez_string:
    print(s)


# Iterating over a dictionary
ez_dict = {1 : "First", 2 : "Second"}
for key, value in ez_dict.items():
    print(key, value)
    
    
# Iterating over a number
number = 12345
for n in number:
    print(n)

# Conversely, objects that do not follow the Iterator protocol 
# cannot be used in a for loop

# Internally next() function is called multiple times for the iterables
# Iterables support something called the Iterator Protocol.  ( iter and next )
# lists, strings and dictionaries all follow the Iterator Protocol    


expertises = ["Novice", "Beginner", "Intermediate", "Proficient", "Experienced", "Advanced"]

expertises_iterator = iter(expertises)
print(type(expertises_iterator))


next(expertises_iterator)
next(expertises_iterator)
next(expertises_iterator)
next(expertises_iterator)
next(expertises_iterator)
next(expertises_iterator)

next(expertises_iterator)

#Internally, the for loop also calls the next function and terminates, 
# when it gets StopIteration. 

other_cities = ["Strasbourg", "Freiburg", "Stuttgart", "Vienna / Wien", "Hannover", "Berlin", 
                "Zurich"]

city_iterator = iter(other_cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        break

# Or
       
for location in other_cities:
    print(location)

'''Difference between a regular function and generator function '''
    
# Regular function
def function_a():
    # a lot of lines here
    return "a"

# Generator function
def generator_a():
    yield "a"


def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")


city = city_generator()
type(city)

print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))

print(next(city))

city = city_generator()
# Start again generating values

#Generators are iterables themselves. 
for item in city:
    print(item)
    

"""skip this
# Generator Expresssion ( Similar to Comprehension)
my_list = ['a', 'b', 'c', 'd']
gen_obj = (x for x in my_list)

type(gen_obj)

next(gen_obj)

for val in gen_obj:
    print(val)
"""


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

primes = Primes(10)

next(primes)
next(primes)
next(primes)

next(primes)

primes = Primes(10)


""" Reading from a long log file """

def gen_records(path):
    with open(path) as handle:
        record = {}
        for line in handle:
            if line == "\n":
                yield record
                record = {}
                continue
            key, value = line.rstrip("\n").split(": ", 1)
            record[key] = value
            
            
for record in gen_records('data.txt'):
    print("{} had {} requests in the past hour".format(
        record["article"], record["requests"]))


"""
Code Challenge
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]

Solution:
'''Running avarage'''

list1 = [7, 13, 17, 231, 12, 8, 3]

def run_avg(list1):
    new_list = []
    for i in list1:
        new_list.append(i)       
        yield str(round(float(sum(new_list))/float(len(new_list)),2))
        
        
char = run_avg(list1)

next(char)



"""

"""
Code Challenge

https://github.com/thecbp/blog_data/blob/master/recipeData.csv

The data contains important beer characteristics from brewers around the world, 
including style of beer, alcohol by volume (ABV), and amount of beer produced.
"""

"""
Code Challenge
Web scraping and crawling recursively for a link
"""

#############

"""
Introduce the concept of Iterators & Generators
https://realpython.com/blog/python/introduction-to-python-generators/

In Python, an iterator is an object which implements the iterator protocol. 
The iterator protocol consists of two methods. The __iter__() method, 
which must return the iterator object, and the next() method, 
which returns the next element from a sequence.


Iterators have several advantages:
    Cleaner code
    Iterators can work with infinite sequences
    Iterators save resources

By saving system resources we mean that when working with iterators, 
we can get the next element in a sequence without keeping the entire dataset in memory. 

Python has several built-in objects, which implement the iterator protocol. 
For example lists, tuples, strings, dictionaries or files. 


Normally, if we want to read from a file in Python, we do so one line at a time, as follows:

    for one_line in open(filename):
        print(one_line.rstrip())

    
But sometimes, we want to read more than one line at a time.

For example, suppose a logfile is written in a three-line format. Reading one line at a time is pretty useless, especially if we want to compare a value on line 1 with a value on line 3.

Reading the entire file into a string isn't what we want, either; it might well be too long for us to read the entire thing.  What I really want to do is read three lines at a time.

For this exercise, I want you to write a generator function that takes two arguments — the filename from which to read, and the maximum number of lines that should be returned with each iteration.  That is, if our file is

    File line 0 aaa
    File line 1 bbb
    File line 2 ccc
    File line 3 ddd
    File line 4 eee
    File line 5 fff
    File line 6 ggg

Then I could do this:

    for two_lines in read_n(filename, 2):
        print(two_lines.rstrip())
    
And the result would be:

   File line 0 aaa
   File line 1 bbb

   File line 2 ccc
   File line 3 ddd

   File line 4 eee
   File line 5 fff

   File line 6 ggg


Notice that the last line is by itself, because there was an odd number of lines.  We could also say:

    for four_lines in read_n(filename, 4):
        print(four_lines.rstrip())

    
This time we get four lines at a time:

   File line 0 aaa
   File line 1 bbb
   File line 2 ccc
   File line 3 ddd

   File line 4 eee
   File line 5 fff
   File line 6 ggg

With each iteration, read_n should return a string (not a list) containing up to the number of lines specified by the second parameter.

Note that read_n isn't a function that returns a list, but rather a generator function.  In other words, executing read_n will return a generator object -- in other words, an object that implements Python's iteration protocol, and thus knows how to behave inside of a "for" loop or list comprehension.

def read_n(filename, n):
    f = open(filename)

    while True:
        output = ''.join(f.readline()
        for i in range(n))
        if output:
            yield output
        else:
            break

for index, chunk in enumerate(read_n('solution.py', 3)):
    print("{0} '{1}'".format(index, chunk))
    
"""




    