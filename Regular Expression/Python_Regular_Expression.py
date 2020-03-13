# Regular Expression

"""
The term "regular expression", sometimes also called regex or regexp, 
is originated in theoretical computer science. 

In theoretical computer science they are used to define a language family 
with certain characteristics, the so-called regular languages.

Regular Expressions are used in programming languages to filter texts or textstrings.

It's possible to check, if a text or a string matches a regular expression.
The syntax of regular expressions is the same for all programming
and script languages, e.g. Python, Perl, Java, SED, AWK and even X#.

Regular expressions was first incorporated in the editor of unix/linux and grep command

Wildcards, also known as globbing, look very similar in their syntax to regular expressions.

The command "ls *.txt" lists all files (or even directories) ending with the suffix .txt; 
in regular expression notation "*.txt" wouldn't make sense, 
it would have to be written as ".*.txt" 

"""
# Open Sample file example-text-regex.txt


'''Normal Searching for a substring in a string'''
s = "Regular expressions easily explained!"
"easily" in s


'''Introduce the concept of raw string using an example'''
print ('\tTab')

print (r'\tTab')



'''First substring matching in a string using Regular Expression'''

import re
x = re.search(r"cat","A cat and a rat can't be friends. but cat and dog can")

print(type(x))

if x is not None:
    print(x.span())
else:
    print(x)


import re
x = re.search(r" cat ","A cat and a rat can't be friends. but cat and dog can")
print (x)

import re
x = re.search(r"cow","A cat and a rat can't be friends. but cat and dog can")
print (x)


'''All substring matching in a string using Regular Expression'''

import re
x = re.finditer(r"cat","A cat and a rat can't be friends. but cat and dog can")
print(type(x))

next(x).span()




'''Any Single Character . matching'''

# recognize all three letter words, which end with "at". 
# ".", which is used like a placeholder for "any character".

# The syntax of regular expressions supplies a metacharacter ".", 
# which is used like a placeholder for "any character".

import re
x = re.finditer(r".at ","A cat and a rat can't be friends. but cat and dog can")
print(type(x))

next(x)

# Short Logic to get all the occurences of substring in the string
[(m.start(0), m.end(0)) for m in re.finditer(r".at ","A cat and a rat can't be friends. but cat and dog can")]


# This RE matches three letter words, isolated by blanks, which end in "at". 
# Now we get words like "rat", "cat", "bat", "eat", "sat" and many others.


'''Character Classes   [ ]'''   
"""
Square brackets, "[" and "]", are used to include a character class. 
[xyz] means e.g. either an "x", or "y" or "z".

[a-e] a simplified writing for [abcde] 
or 
[0-5] denotes [012345].

So instead of [ABCDEFGHIJKLMNOPQRSTUVWXYZ] we can write [A-Z].

Write an expression for the character class "any lower case or uppercase letter" 
[A-Za-z]

So the expression [-az] is only the choice between the three characters "-", "a" and "z", 
but no other characters. 

The same is true for [az-]. 

# What character class is described by [-a-z]? 
# Answer The character "-" and all the characters "a", "b", "c" all the way up to "z”.

"""

# r"M[ae][iy]er"

# This is a regular expression, which matches a surname which is quite common in German.
# A name with the same pronunciation and four different spellings:
# Maier, Mayer, Meier, Meyer

#A finite state automata 




"""

The only other special character inside square brackets (character class choice) is the caret "^”. 
If it is used directly after an opening square bracket, it negates the choice. 
[^0-9] denotes the choice "any character but a digit”. 

The position of the caret within the square brackets is crucial. 
If it is not positioned as the first character following the opening square bracket, 
it has no special meaning. 
[^abc] means anything but an "a", "b" or "c" 
[a^bc] means an "a", "b", "c" or a "^" 
"""


"""
TRY THIS ON SUBLIME TEXT
========================================================
.	        Any Single Character

[abc]       Any character a or b or c, not combination

[abc]{3}    Combination of any a or b or c in three

[a-z]       Any Character a to z

[a-z0-9]    Any Character a to z, Numbers 0 to 9

[a-z0-9_]   Any Character a to z, Numbers 0 to 9 and _

[^abc]      Any Character except a or b or c
            ^ is the negation
========================================================
"""




# quantifier
"""

A quantifier after a token, which can be a single character or group in brackets, 
specifies how often that preceding element is allowed to occur. 
The most common quantifiers are

?           zero or exactly one
*           zero or more
+           one or more 

"""


r"[0-9]*"
#The above expression matches any sequence of digits, even the empty string. 


r".*" 
#matches any sequence of characters and the empty string. 


# Exercise:
# Write a regular expression which matches strings which starts with a 
# sequence of digits - at least one digit - followed by a blank.

# Solution:
r"^[0-9][0-9]* "

# Solution with the plus quantifier:
r"^[0-9]+ "



"""
TRY THIS ON SUBLIME TEXT
========================================================
[a-c]+\.{4}[d-f]+


[a-c]+   means one or more
abc... will not be selected
...def will not be selected 



[a-c]*\.{4}[d-f]*
[a-c]* means zero or more 


[a-c]?\.{4}[d-f]?
[a-c]? means zero or exactly one 




?           zero or exactly one
*           zero or more
+           one or more 
========================================================
"""

"""
	{m}	        m Repetitions

	{m,n}	    m to n Repetitions

	*	        Zero or more repetitions

	+	        One or more repetitions

	?	        Zero or one
    
"""


"""
========================================================
match       gives index if its in the beginining 

search      gives index for first and every occurence

findall     does not return index but a list

finditer    iterates through all the searched indexes

========================================================
"""

import re

result = re.search(r'forsk','Forsk forsk Summer Bootcamp')

print(result)

print(result.start())
print(result.end())

dir(result)



result = re.match(r'forsk','Forsk forsk Summer Bootcamp')

print(result.start())
print(result.end())



result = re.match(r'Forsk','Forsk forsk Summer Bootcamp')

print(result.start())
print(result.end())





import re

text_to_search = r"""Start""" 

sentence = "Start a sentence and then bring it to end after the Start"

pattern = re.compile (text_to_search)

pattern.search(sentence)

pattern.match(sentence)

pattern.findall(sentence)

 

"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement:
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
     re.search(r"J.*Neu",line)  
 Solution:
     Jack Neu 555-7666
     Jeb Neu 555-5543
     Jennifer Neu 555-3652
"""



# Predefined Character Classes

"""
The special sequences consist of "\\" and a character from the following list:
\d  Matches any decimal digit; equivalent to the set [0-9].
\D  The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].

\s  Matches any whitespace character; equivalent to [ \t\n\r\f\v].
\S  The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].

\w  Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.
\W  Matches the complement of \w.

\b  Matches the empty string, but only at the start or end of a word.
\B  Matches the empty string, but not at the start or end of a word.

\\  Matches a literal backslash.

"""

"""
TRY THIS ON SUBLIME TEXT
========================================================
\d          One Digit

\d\d        Two Digits

\d\d\d      Three Digits

\d{3}       Minimum Three Digits

\d{3,6}     Minimum Three, Maximum Six Digits

\d{3, }     Minimum Three, Maximum not set

\d{, 6}     Not Possible

\D          Any non Digit

\.          Only dot

\.{3}       Three dots

========================================================

"""

#all meta characters needs to be escaped if we want it to be searched
# . ^ $ + ? { } [ ] \ | ( ) 


# . is for any character except new line
pattern = re.compile (r'\.')

# d is for digit 0 to 9
pattern = re.compile (r'\d')

# D is for not a digit 0 to 9
pattern = re.compile (r'\D')

# w is for word character (a-z, A-Z, 0-9, _)
pattern = re.compile (r'\w')

# W is for not a word character (a-z, A-Z, 0-9, _)
pattern = re.compile (r'\W')

# s is for white space (space, tab, new line)
pattern = re.compile (r'\s')

# S is for not a white space (space, tab, new line)
pattern = re.compile (r'\S')

# b is for word boundary ( white space or alpha numeric )
pattern = re.compile (r'\bHa')

# B is for word boundary
pattern = re.compile (r'\BHa')

# ^ is for beginning of a string
pattern = re.compile (r'^Start')

# $ is for end of a string
pattern = re.compile (r'end$')




# Matching Phone Numbers 
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 321–555--4321
# 900-555-1234
# 800-555-1234

# This will match any seperator between the numbers  
pattern = re.compile (r"\d\d\d.\d\d\d.\d\d\d\d")

# This will match . and - seperator between the numbers  using character set 
pattern = re.compile (r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")

# Match the 800 or 900 numbers 
pattern = re.compile (r"[89]00[-.]\d\d\d[-.]\d\d\d\d")
 
# matches digits between 1 and 5
pattern = re.compile (r'[1-5]')

# matches characters between a and z
pattern = re.compile (r'[a-z]')

# matches characters between a and z and A to Z also
pattern = re.compile (r'[a-zA-Z]')


# ^ negates within a character set 
# but if used within a string then it marks the beginning 
pattern = re.compile (r'[^a-zA-Z]')


# matches cat mat and pat but not bat
# ending should be at but the beginning should not be with b
pattern = re.compile (r'[^b]at')





"""
# using quantifier to match multiple characters at a time 
?   -   0 or exactly one 
* -   0 or more
+ -   1 or more
{3} - Exact Number
{3,4} - Range of Number (min, max)
"""

# This will match any seperator between the numbers  
pattern = re.compile (r"\d{3}.\d{3}.\d{4}")
 


# Reading only phone numbers from a text file

pattern = re.compile (r"\d\d\d.\d\d\d.\d\d\d\d")

with open ("data.txt","r", encoding='utf-8') as f:
    contents = f.read()

matches = pattern.finditer(text_to_search)

for match in matches :
    print ( match )
    


"""
Mr. Sylvester
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

# Matches the above prefixes  with Mr.  
pattern = re.compile (r"Mr\.")
 
pattern = re.compile (r"Mr\.?")

pattern = re.compile (r"Mr\.?\s[A-Z]")

pattern = re.compile (r"Mr\.?\s[A-Z]\w*")

""" 
|   Either or
( ) Group
"""


# using group ( )  to match a multiple 
pattern = re.compile (r"M(r|s|rs)\.?\s[A-Z]\w*")

pattern = re.compile (r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")






emails = """
SylvesterFernandes@gmail.com
sylvester.fernandes@university.edu
sylvester-321-fernandes@my-work.net
"""



# Match all of the emails 
# + will match one or more 
pattern = re.compile (r"[a-zA-Z]+@[a-zA-Z]+\.com")

pattern = re.compile (r"[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)")


pattern = re.compile (r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")






# Reading someone else regex 

urls = """
https://www.google.com
http://forsk.in
https://youtube.com
https://www.nasa.gov
"""
pattern = re.compile (r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")



# Sample regex 1

pattern = re.compile (r"^[a-z0-9_-]{3,16}$")

"""
Starts and ends with 3-16 numbers, letters, underscores or hyphens
Any lowercase letter (a-z), number (0-9), an underscore, or a hyphen.
At least 3 to 16 characters.
Matches E.g. my-us3r_n4m3 but not th1s1s-wayt00_l0ngt0beausername
"""


# Sample regex 2

pattern = re.compile (r"^[a-z0-9_-]{6,18}$")

"""
Starts and ends with 6-18 letters, numbers, underscores, hyphens.
Matches e.g. myp4ssw0rd but not mypa$$w0rd
"""


# Sample regex 3

pattern = re.compile (r"^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$")

"""
String that matches: john@doe.com
String that doesn't match: john@doe.something (TLD is too long)
"""


# Sample regex 4
mobile="""
+9999999999
999999-999
99999x9999
"""

pattern = re.compile (r"(\+[8-9]{1}[0-9]{9})")

pattern = re.compile (r"^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$")







"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""

"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""

"""

Code Challenge
  Name: 
    Regular Expression 3
  Filename: 
    regex3.py
  Problem Statement:
    You and Virat are good friends. 
    Yesterday, Virat received credit cards from ABCD Bank. 
    He wants to verify whether his credit card numbers are valid or not. 
    You happen to be great at regex so he is asking for your help!

    A valid credit card from ABCD Bank has the following characteristics:

    It must start with a '4', '5' or ' 6'.
    It must contain exactly 16 digits
    It must only consist of digits (0-9)
    It may have digits in groups of 4, separated by one hyphen "-"
    It must NOT use any other separator like ', ' , '_', etc
    It must NOT have 4 or more consecutive repeated digits 
 
  Hint: 
    Using Regular Expression 
  Input:
    4123456789123456
    5123-4567-8912-3456
    61234-567-8912-3456
    4123356789123456
    5133-3367 -8912-3456
    5123 - 3567 - 8912 - 3456
  Output:
    Valid
    Valid
    Invalid
    Valid
    Invalid
    Invalid
"""

"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

"""

"""

Code Challenge
  Name: 
    Post Codes UK
  Filename: 
    postcodes_uk.py
  Problem Statement:
    We write an expression, which is capable of recognizing the postal codes or postcodes of the UK.

    Postcode units consist of between five and seven characters, 
    which are separated into two parts by a space. 
    
    The two to four characters before the space represent the so-called outward 
    code or out code intended to direct mail from the sorting office to the delivery office. 
    
    The part following the space, which consists of a digit followed by two uppercase characters, 
    comprises the so-called inward code, which is needed to sort mail at the final delivery office. 
    
    The last two uppercase characters do not use the letters CIKMOV, 
    so as not to resemble digits or each other when hand-written.

    The outward code can have the form: One or two uppercase characters, 
    followed by either a digit or the letter R, 
    optionally followed by an uppercase character or a digit. 
    (We do not consider all the detailed rules for postcodes, 
    i.e only certain character sets are valid depending on the position 
    and the context.)    
  Hint: 
    Using Regular Expression 
  Input:
      example_codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwhich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
                ]

"""

"""

Code Challenge
  Name: 
    Post Codes Germany
  Filename: 
    postcodes_germany.py
  Problem Statement:
    We have to bring together the information of two files. 
    In the first file, we have a list of nearly 15000 lines of post codes with the 
    corresponding city names plus additional information. 

    The other file contains a list of the 19 largest German cities. 
    Each line consists of the rank, the name of the city, the population, 
    and the state (Bundesland): 
    
    Our task is to create a list with the top 19 cities,
    with the city names accompanied by the postal code. 
    If you want to test the following program, 
    you have to save the list above in a file called largest_cities_germany.txt 
    and you have to download and save the list of German post codes

  Output:
    The output of this file looks like this, 
    but we have left out all but the first three postal codes for every city: 
    
        Berlin {'10715', '13158', '13187', ...}
        Hamburg {'22143', '22119', '22523', ...}
        München {'80802', '80331', '80807', ...}
        Köln {'51065', '50997', '51067', ...}
        Frankfurt am Main {'65934', '60529', '60308', ...}
        Essen {'45144', '45134', '45309', ... }
        Dortmund {'44328', '44263', '44369',...}
        Stuttgart {'70174', '70565', '70173', ...}
        Düsseldorf {'40217', '40589', '40472', ...}
        Bremen {'28207', '28717', '28777', ...}
        Hannover {'30169', '30419', '30451', ...}
        Duisburg {'47137', '47059', '47228', ...}
        Leipzig {'4158', '4329', '4349', ...'}
        Nürnberg {'90419', '90451', '90482', ...}
        Dresden {'1217', '1169', '1324', ...}
        Bochum {'44801', '44892', '44805', ...}
        Wuppertal {'42109', '42119', '42287', ...}
        Bielefeld {'33613', '33607', '33699', ...}
        Mannheim {'68161', '68169', '68167', ...}
      
  Hint: 
    Using Regular Expression 
    zuordnung_plz_ort.csv
    list of nearly 15000 lines of post codes with the corresponding city names 
    plus additional information.

"""

# Add a challenge for german postal code
# file already present in data folder 
# post_codes_germany.txt



# Sublime Text Story Telling
"""
CMD + F     Normal Search  ( easily )

# Change the searching from Normal to Regular Expression based 
========================================================
\d          One Digit

\d\d        Two Digits

\d\d\d      Three Digits

\d{3}       Minimum Three Digits

\d{3,6}     Minimum Three, Maximum Six Digits

\d{3, }     Minimum Three, Maximum not set

\d{, 6}     Not Possible

\D          Any non Digit

\.          Only dot

\.{3}       Three dots

========================================================
.	        Any Single Character

[abc]       Any character a or b or c, not combination

[abc]{3}    Combination of any a or b or c in three

[a-z]       Any Character a to z

[a-z0-9]    Any Character a to z, Numbers 0 to 9

[a-z0-9_]   Any Character a to z, Numbers 0 to 9 and _

[^abc]      Any Character except a or b or c
            ^ is the negation

========================================================

\w          Any alphanumeric character

\W          Any non alphanumeric character
========================================================

\s          Any whitespace

\S          Anything other than whitespace

========================================================

abc

^abc        Starts with abc


def 

def$        Ends with DEF



^ and $ are meta chracters

 
ABC 

^ABC

ABC$        Searches ABC in the last 

ABC\$       Searches ABC$  
 
ABC\$$      Searches ABC$ in the last 


(abc|def)   Searchs abc or def



========================================================

[a-c]+\.{4}[d-f]+


[a-c]+   means one or more
abc... will not be selected
...def will not be selected 



[a-c]*\.{4}[d-f]*
[a-c]* means zero or more 


[a-c]?\.{4}[d-f]?
[a-c]? means zero or exactly one 




?           zero or exactly one
*           zero or more
+           one or more 
========================================================
^[a-z0-9_-]{3,16}$

Start with and end with, so in between 
Password validation
========================================================
  
match       gives index if its in the beginining 

search      gives index if for first and every occurence

findall     does not return index but a list
========================================================

"""


"""

https://lerner.co.il/courses/regular-expressions/

Regular expressions

Course length: 2 days (16 hours)

Description: 
Regular expressions (“regexps”) make it possible to find patterns inside of text. 

Whether you’re trying to find all of the URLs in a document, or the IP addresses 
in a logfile,  or telephone numbers in an address book, regular expressions 
can be invaluable — and thus are included in most modern programming languages, 
such as Python, Ruby, and JavaScript, as well as .NET, Java, and C++. 

Many utilities, such as Unix’s famous “grep” command, are popular because they 
use regular expressions. However powerful regular expressions might be, they 
are also famously difficult to write, and even more difficult to read. 

Many experienced programmers find themselves frustrated by the syntax of 
regular expressions, and either avoid them entirely or use pre-packaged recipes
they find on the Internet.

This course introduces regular expressions, and provides numerous insights into
their many features and uses. It will also point to differences between dialects 
of regular expressions, ways in which they should (and shoudn’t) be used, 
Advanced techniques such as named groups and lookahead/lookbehind.

By the end of the course, participants should feel comfortable using 
regular expressions to find and analyze text.
A large part of the course will be hands-on exercises, which will help 
participants to learn and understand the regular expression syntax.

Audience: 
This course is aimed at experienced programmers who wish to unlock 
the power of regular expressions in their day-to-day work. 
While nearly all exercises will be in the Python language, little or no 
knowledge of Python is necessary; the course will begin with a very brief 
introduction to the Python features needed to do the exercises.


Course syllabus

    Minimal Python for text processing
        Strings
        Lists
        Loops
        Files
    Overview of regular expressions
        Python’s “re” module
        re.find
        re.search
        re.findall
        match objects
    Characters and metacharacters
    Multiple runs of a character
        +
        *
        {min,max}
    Debugging regexps
    Character classes
        []
        ^
        $
        –
    Built-in character classes
        \w \W
        \s \S
        \d \D
        Greediness
        Anchors
        Start/end of line
        Start/end of string
        Start/end of word
    Options
        Case
        Line endings
        Extended regexps with comments
    Alternation
        Parentheses for combining
        Parentheses for capturing
        Non-capturing parentheses
        Named groups
        Backreferences
    Raw strings, backslashes, and regexps
    Lookahead/lookbehind
    Conditionals
    Handling Unicode
        Bytes vs. characters
        Matching Unicode characters
        Sets of Unicode characters
    Compiling regexps
    Replacing regexps
    Match context
    Development and debugging strategies
    Efficiency
    Regexps in JavaScript
    Regexps in Ruby
    Regexps in Unix
    When are regexps not useful?
    Useful resources


"""