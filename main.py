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