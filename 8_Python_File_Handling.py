"""
Important Operating System related file handling
"""      
import os

os.getcwd()  ## show current working directory

os.chdir(r"C:\Users\Windows10\Desktop")  ## change directory

os.getcwd()

os.path.exists("age_cal.py")  ## True

os.path.exists("data/zoo.csv")   ## False

os.remove("new.txt")  ## remove file

os.makedirs("myfolder")  ## make new folder

os.rmdir("myfolder")   ## remove folder

os.listdir(".")
###################################################

# File handling in Python 

"""
There are two types of files
1. Text File
    contains Human Readble data
    E.g. Plain text file, XML, JSON, Source Code
    
2. Binary File
    used to store compiled code, app data, media data
    non human readable
    E.g. images, audio, video
"""

f = open("test.txt")    ## by default read mode is used
# perform file operations
f.close()

file = open("words.txt")
print (file.name)
print (file.mode )
print (file.closed)  ## return False

file.close() 

print (file.closed )  ## return True

dir(file)

"""
There are four different methods (modes) for opening a file
  "r" - Read
  "a" - Append
  "w" - Write 
  "x" - Create 

In addition you can specify if the file should be handled as binary or text mode
  "t" - Text - Default value. Text mode
  "b" - Binary - Binary mode (e.g. images)
"""

file = open("words.txt",  "rt" )
print (file.name)


# Exception Handling in File Handling
try:
    file = open("words1.txt",  "rt" )
    print (file.name)
except IOError:
    print ( "File not Found or incorrect path")
except Exception:
    print ( "This is a general exception")
finally:
    print ("this is called always")
    file.close() 

"""
Context Manager to open the File 
( Automatically closes the file after using in the block ) 
"""

with open('words.txt', mode='rt') as f :
    # perform your operations within this block 
    pass


with open('words.txt', mode='rt') as file :
   file_contents = file.read()      ## read whole content of file
   print (file_contents)
   
   
with open('words.txt', mode='rt') as file :
   file_contents = file.readline()    ## read 1st line
   print (file_contents)
   
   file_contents = file.readline()    ## then read 2nd line and so on for further
   print (file_contents)


with open('words.txt', mode='rt') as file :
   file_contents = file.readlines()   ## return a list consist of lines of file
   print (file_contents)


with open('words.txt', mode='rt') as file :
   for line in file:    ## same as readlines()
       print (line)

with open('words.txt', mode='rt') as file :
   file_contents = file.read(4)   ## read 4 bytes means 4 characters
   print (file_contents)          ## 1st letter start from 1 index not from 0


''' 
method tell() : returns the current position of the file read/write pointer
'''
file = open("words.txt", "rt")

position = file.tell()   ## 0 in starting
print (position)

line = file.readline()
print (line )

position = file.tell()  ## after reading the lines it becomes 12
print (position)

''' 
The method seek(): sets the file's current position at the offset.
  
# file.seek(offset[, whence])
# offset − This is the position of the read/write pointer within the file.
# whence − defaults to 0 which means absolute file positioning,
#          1 which means seek relative to the current position,
#          2 means seek relative to the file's end
'''
line = file.readline()
print (line)
   
position = file.tell()
print (position)
    
file.seek(0,0)      ## pointer, start(0) from 0
position = file.tell()
print (position)

file_contents = file.read(6)
print (file_contents)

position = file.tell()
print (position)

file.seek(0,1)     ## pointer, start from the current position of pointer
file_contents = file.readline()
print (file_contents)

lines = file.readlines()
print (lines)

position = file.tell()
print (position)


"""
How to create and write into Files
"""
# print(variable,file=f)
file = open('new.txt', mode='wt')    ## file open if exist otherwise created

file.write("Now this has one line\n")
file.writelines(["Second Line\n", "Third Line\n"])

file.close()
## write mode overwrites the content.


"""
How to read and write non text files
"""
with open ("a.jpg", "rb") as rf :
  with open ("b.jpg", "wb") as wf :
    for line in rf :
      wf.write ( line)

###############################################################

"""
PIL ( PILLOW LIBRARY )
"""
from PIL import Image
import os

os.chdir(r"C:\Users\Windows10\Desktop")  ## change directory

# Open the image and create it's instance
img = Image.open("Bikesgray.jpg")

# Gives the dimensions or the size of the image
print (img.size)

# Gives the width of the image
print (img.width)

# Gives the height of the image
print (img.height)

# Gives the format of image like JPEG, PNG ...
print (img.format)

# Gives the mode of image like RGB, binary, GreyScale ...
print (img.mode)

# Displays the Image
img.show()

# Rotate the image with the given angle
# Create separate instance for rotated image
# ROTATE_90, ROTATE_180, ROTATE_270 anticlockwise
img_rotate = img.transpose(Image.ROTATE_900)
 
# Displays the rotated image
img_rotate.show()  

img_rotate.save("bike2.jpg")

os.path.exists("bike2.jpg")
os.listdir('.')


# Resizing the image 
small_im = img.resize((300, 150), resample=Image.BICUBIC)
small_im.show()
small_im.save('small_bike.jpg')


# Creating Thumbnail
img = Image.open("bike2.jpg")
img.thumbnail((150, 100))
print(img.width, img.height)
img.save('thumb_bike.jpg')


# Cropping
img = Image.open("bike2.jpg")
                  # startx,starty,width,height
crop_im = img.crop(box=(340, 20, 560, 164))
crop_im.save('crop_bike2.jpg')
crop_im.show()


# Adding a Border
img = Image.open("Bikesgray.jpg")
border_im = Image.new('RGB', (img.width+20, img.height+20), 'yellow')
border_im.paste(img, (10, 10))
border_im.show()
border_im.save("border_bike.jpg")
os.path.exists("border_bike.jpg")


# Flip the image
# Create separate instance for flipped image
# FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM
img_flip = img.transpose(Image.FLIP_TOP_BOTTOM)

# Displays the rotated image
img_flip.show()  
img_flip.save("bike3.jpg")


# Make Black and White image
img_bw = Image.open("exercise.jpg")
img_bw.convert(mode='L').save('exercise2.jpg')
img_bw.show() 


# Blur the Images 
from PIL import Image, ImageFilter
img_blur = Image.open("exercise.jpg")

# 15 is the radius, default is 2 so it doesn’t show too much 
img_blur.filter(ImageFilter.GaussianBlur(4)).save('exercise3.jpg')
img_blur = Image.open('exercise3.jpg')
img_blur.show()

################################################################

"""
Playing with csv files
"""
"""
For example, you might export the results of a data mining program to a CSV file and
then import that into a spreadsheet to analyze the data, generate graphs for a
presentation, or prepare a report for publication.

A CSV file (Comma Separated Values file) is a type of plain text file that uses
specific structuring to arrange tabular data.

Because it's a plain text file, it can contain only actual text data
—in o.ther words, printable ASCII or Unicode characters.

Normally, CSV files use a comma to separate each specific data value.

The first row is known as a header. There is no data type for the data.

In general, the separator character is called a delimiter, and the comma is not the
only one used. Other popular delimiters include the tab (\t), colon (:) and 
semi-colon (;).

Two comma means the data is mising
"""
import os
os.chdir(r"C:\Users\Windows10\Desktop\Data_Science\Pandas\pd_csv")

for line in open("Salaries.csv"):
    print( line )

for line in open("Salaries.csv"):
    print(line.strip() )     ## remove space from left and right

for line in open("Salaries.csv"):
    print( line.strip().split() )

lines = [line.strip().split() for line in open("Salaries.csv")]

lines[0] # List of Headers
lines[1] # List of Data


# Drawback is that all the data is string 
# What if the data itself contains commas    
import csv

print(dir(csv))

with open("Salaries.csv") as csv_file:
    data =[]
    csv_reader = csv.reader(csv_file, delimiter=",")
    # row has the list of all columns
    for row in csv_reader:
        data.append(row)
        print (row)
    # data = [row for row in csv_reader]


# You can convert each column data into specific data type accordingly 
# Printing  a specific column    
import csv

with open("Salaries.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # row has the list of all columns
    for row in csv_reader:
        print ( row[0] )


# Skipping a header line or first line
import csv

with open("Salaries.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the first row
    next(csv_reader)
    # row has the list of all columns
    for row in csv_reader:
        print (row)


# Reading as a Dictionary       
import csv

with open("Salaries.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        print ( row )
        #print ( row['discipline'] )
        #print ( row['salary'] )
        #print ( row['service'] )
        #print ( row['rank'] )
        #print ( row['sex'] )
        #print ( row['phd'] )

"""
Creating a csv file
"""
import csv

with open('employee.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    # We have skipped writing the header
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])









