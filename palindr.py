"""
Name: 
    Centered Average         
Filename:
    centered.py
Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is the 
    mean average of the values, except ignoring the largest and smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. Use int division to produce the final average. 
    You may assume that the array is length 3 or more.
    Take input from user
Sample Input:
    1, 2, 3, 4, 100 
Sample Output:
    3 
""" 
# take input list

#lis1= [1, 2, 3, 4, 100]
#lis1.remove(min(lis1))
#lis1.remove(max(lis1))
#print(lis1)
#
#avg= sum(lis1)//len(lis1)
#print(avg)




"""
Name: 
    Unlucky 13         
Filename:
    unlucky.py
Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user
Sample Input:
    13, 1, 2, 13, 2, 1, 13 
Sample Output:
    3 
""" 
# take input list
##lis2= [13, 1, 2, 13, 2, 1, 13]
#lis2= [1, 13, 1, 2, 5, 2, 13, 2, 1, 13, 9]
#ind=0
#lsum=0
#flag= False
##while(ind<= len(lis2)):
#for num in lis2:
#    if num== 13: or flag==1
#        flag=1
#        continue
#    else:
#        lsum+= num
#        
#print(lsum)




"""
Name: 
    Pangram         
Filename:
    pangram.py
Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM. 
Hint: 
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.  
Sample Input:
    The five boxing wizards jumps. 
    Sphinx of black quartz, judge my vow.
    The jay, pig, fox, zebra and my wolves quack!
    Pack my box with five dozen liquor jugs.
Sample Output:
    NOT PANGRAM 
    PANGRAM
    PANGRAM
    PANGRAM
"""  
str1= 'Pack my box with five dozen liquor jugs.'
alph= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

str2= ''
str2+= str1.lower() 
print(str2)
flag= 0

for char in alph:
    if char in str2:
        flag= 1
    else:
        flag= 0
        break

print(flag)
if flag==1:
    print('PANAGRAM')
else:
    print('NOT PANAGRAM')





from random import randrange

rank= ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
suit= ['clubs(♣)', 'diamonds(♦)', 'hearts(♥)', 'spades(♠)']
card= []

for val in range(20):
    a= randrange(13)
    b= randrange(4)
    while((a,b) not in card):
        card.append((a,b))
        if b in [1,2]:
            print("\033[1;31;47m {} {} ".format(rank[a],suit[b]))
        else:
#            print('\033[30m') # and reset to default color
#            print('card:',rank[a],suit[b])
            
            print("\033[1;30;47m {} {} ".format(rank[a],suit[b]))
    
print('\nTotal cards generated:',len(card))




print("\033[1;32;47m Bright Green  \n") 

''' for color in text, make diamond and heart red else remain'''




from colorama import Fore, Back, Style 

print(Fore.RED + 'some red text') 

print(Fore.GREEN + 'and with a green background') 

#print(Style.DIM + 'and in dim text') 
#print(Style.RESET_ALL) 
#print('back to normal now') 



from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

# then use Termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))






"""
Name: 
    Sorting         
Filename:
    sorting.py
Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score   
Sample Input:
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
Sample Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
""" 

lis1= [('Tom', 19, 80), ('John',20,90), ('Jony',17,91), ('Jony',17,93), ('Json',21,85)]

# sort name wise
lis1.sort()
print(lis1)

# sort age wise
lis1.sort(key= lambda x: x[1])
print(lis1)

# sort height wise
lis1.sort(key= lambda x: x[2])
print(lis1)





print('\033[1m' + 'Hello' + '\033[0m')

print ('\033[0m')



#from __future__ import unicode_literals, print_function
from prompt_toolkit import print_formatted_text, HTML

print_formatted_text(HTML('<b>This is bold</b>'))
print_formatted_text(HTML('<i>This is italic</i>'))
print_formatted_text(HTML('<u>This is underlined</u>'))






