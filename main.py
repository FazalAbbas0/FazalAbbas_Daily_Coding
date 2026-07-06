# Python foundations for FastAPI
# Virtual Environment
#=====================================
# DAY 0 - virtual environment and installation
#======================================
"""
Create a virtual environment
Every python project on your machine required system wide
python installation otherwise you tell it. different version 
of same libraries required would crash each other silently.
Virtual environment is a self contained folder with python
interpreter and installed packages.
python -m venv .venv
Activattion of the virtual environment
.venv\Scripts\Activate.ps1
python versions
python --version
deactiate the virtual environment
deactivate
you would do all installation of packages inside the virtual
environment. You can also create a requirements.txt file to
list all the dependencies of your project. This file can be
used to recreate the environment on another machine or share
it with others. """
# Pip installation and tracking dependencies
# pip install "fastapi[standard]"
# pip list
# pip freeze > requirements.txt
# pip install -r requirements.txt
# Three Ways to run python
# REPL - python
# Application - python <filename>.py
# jupyter notebook - jupyter notebook
# REPL is a read-eval-print-loop, an interactive shell that
# allows you to execute python code line by line.
# Application is a script that can be run from the command line
# or terminal. it is for building real projects and to add your 
# code in projects.
# jupyter notebook is a web-base interactive environment that
# allows you to create and share documents that contain live
# code, equations, visualizations, and narrative text.
#=========================
# DAY 1 - Syntax, variables and full operators set
#==================================
# Variables the name bound to objects not boxes, that is the 
# signle essential mental model to built required and necessary 
# when you reached mutuable collections.
width = 50
height = 100
area = width * height
print(area)
# Comment is started from # sign. the line inverted commas
#  whereas # sign also would be called string not comment.
# Arithmetic operators
# Addition: +
# Subtraction: -
# multiplication: *
# Ture Division: / , Always returns a float.
# Floor Division: //, Always returns int.
# Modulus: % , Always returns the remainder of the division.
# Exponentiation: **, Always returns the power of the number.
# The full operator Set
# Comparison operators
# ==, !=, >, <, >=, <=
# logical operators - combine boolean values
# and, or not
# Augmented assignment operators - shorthand for self modification
x = 5
x += 3  # equivalent to x = x + 3
x -= 2  # equivalent to x = x - 2
x *= 4  # equivalent to x = x * 4
x /= 2  # equivalent to x = x / 2
x //= 3  # equivalent to x = x // 3
x %= 2  # equivalent to x = x % 2
x **= 3  # equivalent to x = x ** 3
print(x)
# Identity - same object in memory
a = 45
b = 25
a is b
a is not b
# membership
3 in [1, 2, 3]
3 not in [1, 2, 3]
#===================================
# Day 2 - String, Slicing, Creation and formating
#===================================
# Creation and escaping
# Single Quotes: 'Hello'
# Double Quotes: "Hello"
# Triple Quotes: 
"""
Strings - span 
"""
'doesn\'t' # Escaping single quote
'r C:\new\folder' # Escaping backlash
# Indexing and slicing
word = 'Python'
# p  y  t  h  o  n
# 0  1  2  3  4  5
# Negative indexing
# -6 -5 -4 -3 -2 -1
word[0] # 'P'
word[-1] # 'n'
word[0:2] # 'Py'
word[2:5] # 'tho'
word[2:] # 'thon'
word[:2] # 'Py'
word[:] # 'Python'
# f strings the modern standard
name, score = "Fazal", 91.5
f"{name}, scored {score:.1f}%" # fazal scored 91.5%
f"{score=}" # score = 91.5 debug shorthand
# method toolbox
s = "Hello, World!"
len(s)
s.upper();
s.lower();
s.title();
s.strip();
s.title();
s.replace("World", "Python");
s.removeprefix("Hello, ");
s.removeprefix("Hello, ");
s.removesuffix("!");
s.split(", ");
s.partition(", ");
s.find("World");
s.isalnum();
s.isalpha();
s.isupper();
# ===========================================
# Day 3, lists, mutabality, aliasing and copies
# =========================================
squares = [1, 4, 9, 16, 25]
squares[0] # 1
squares[-1] # 25
squares[0:3] # [1, 4, 9]
squares[:3] # [1, 4, 9]
squares[3:] # [16, 25]
squares[:] # [1, 4, 9, 16, 25]
full = squares + [36, 49, 64, 81, 100]
# Mutability changing a list in place
cubes = [1, 8, 27, 65, 125] # something is wrong here
cubes[3] = 64 # replace the wrong value
cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # add the cube of 7
cubes.insert(4, 4 ** 3) # insert the cube of 4 at position 4
cubes.remove(64) # remove the cube of 4
cubes.pop() # remove the last item
cubes.sort() # sort the list
cubes.reverse() # reverse the list
#===================================================
original = ["Red", "Green", "Blue"]
ref = original
copy = original[:]
copy2 = original.copy()
import copy as copy_module
deep = copy_module.deepcopy(original)

#==========================================
# Delete, comprehension and nesting
#=========================================
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] # delete the first element
del a[2:4] # delete the third and fourth elements
del a[:] # delete all elements
square = [x ** 2 for x in range(10)] # list comprehension
positive = [x for x in (-2, -1, 0, 1, 2) if x >= 0] #   list comprehension with condition
vec = [[1,2,], [3,4]]
flattened = [num for row in vec for num in row] # nested list comprehension
#=========================================
# Type - predict run drill - the aliasing gotcha live
#========================================
orginal = ["Red", "Green"]
ref = original
ref.append("Blue")
print(original) # ['Red', 'Green', 'Blue']
copy = original[:]
copy.append("yellow")
print(original) # ['Red', 'Green', 'Blue']