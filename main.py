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
#=============================================
# Day 04 - Sets
#============================================
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# duplicate elements are automatically removed
basket # {'apple', 'orange', 'pear', 'banana'}
empty_set = set() # Create an empty set not dictionary
'orange' in basket # True 0(1) membership test
a = set('abracadabra')
b = set('alacazam')
a-b # difference letters in a but not in b
a | b # union letters in a or b or both
a & b # intersection letters in both a and b
a ^ b # symmetric difference letters in a or b but not both
#====================================================
# Day -04  - The Collections module - new material
#=====================================================
# This sits in directly in the standard library and sits one import away and you will sit in almost every non-trivial python codbase you read. Skipping this is the kind of gap that make someone else's real code look unfamiliar every know every keyword init technicly.
# counter - frequency counting without writing a loop
from collections import Counter
votes = ['py', 'js', 'py', 'go', 'py', 'js']
tally = Counter(votes)
# Conter({'py': 3, 'js': 2, 'go': 1})
tally.most_common(1) # [('py', 3)]
# Default dictionaries that never generate error on first touch
from collections import defaultdict
groups = defaultdict(list)
groups['active'].append('user1')
groups['active'].append('user2')
# groups -> {'active': ['user1', 'user2']}
# named tuples - a tuple with named filds, the ancestor of pydantic models
from collections import namedtuple
point = namedtuple('Point', ['x', 'y'])
p = point(3, 4) 
p.x, p.y # 3, 4          # 3,4 by name not just by index
p[0], p[1] # 3, 4        # 3 4 still works positionaly too
#=========================================================
# Day 05 - Dictionaries, Looping Techniques, Control Flow and matching
#=========================================================
#========================================================
#          Day 05     -    Dictionaries
#========================================================
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127 # add a new key-value pair
tel['jack'] # Direct access - key error if missing
tel.get('irv')  # Safe access - returns None if missing
tel.get('irv', 'unknown') # Safe access with default value
del tel['sape'] # delete a key-value pair
'guido' in tel # check if a key exists
list(tel) # keys in insertion order
sorted(tel) # sorted keys
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # create a dictionary from a list of tuples
squares = {x: x ** 2 for x in (2, 4, 6)} # dictionary comprehension
#========================================================
#        Day 05     -    Looping Techniques
#========================================================
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'color']
answers = ['lancelot', 'grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}.')
#======================================================================
#      Day 06     -    Functions, *args, **kwargs and Decorators
#===================================================================
#                 Functions
#===================================================================
# Functions basics and the mutable-default trap
def fib2():
    "Return fibonacci series below n as list."
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
        return result
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
#======================================================================
#     Day 06     -    *args, **kwargs 
#===================================================================
def cheeseshop(kind, *arguments, **keywords):
    print(f'----Do you have any {kind}?')
    for arg in arguments:
        print(arg)
    for key, val in keywords.items():
        print(f'{key}: {val}')
# unpacking the other direction
args = [3, 6]
list(range(*args)) # [3, 4, 5]
d = {"voltage": high, "state": "dead"}
def parrot(voltage, state): pass
parrot(**d) # equivalent to parrot(voltage=high, state='dead')
#======================================================================
#   Day 06     -    Positional only and keywords only parameters
#===================================================================
def combined(pos_only, /, standard, *, kwd_only):
    # pos_only , must be passed positionally
    # Standard, positional or keyword
    # kwd_only, must be passed as keyword
    pass
#======================================================================
#   Day 06     -    Lambada and Annotations
#===================================================================
pairs = [(1, 'one'), (2, 'two')]
pairs.sort(key=lambda pair: pair[1])
def f(ham: str, eggs: str = 'eggs') -> str:
    """concise one-line summary."""
    return ham + ' and ' + eggs
#======================================================================
#  Day 06     -    Decorators
#===================================================================
# The core idea built from nothing
def shout(func):
    def wrapper(*args, **kwargs):
        return result.upper()
    return wrapper

def greet(name):
    return f'hello {name}'
greet = shout(greet) # manualy wrapping this is what @ does
greet('fazal') # 'HELLO FAZAL'

def shout (func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@shout
def greet(name):
    return f' hellow {name}'
greet('fazal') # 'HELLO FAZAL'
# Decorators that take their own arguments - the @ app.get('/path')shape
def repeate(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
            return wrapper
        return decorator
    
@ repeat(times=3)
def announce():
    print('deployed')

announce() # prints 'deployed' three times
#==========================================================================
# Day 07     -    Modules, Packages, File I/O and Exception handling
#=======================================================================
#           Day -07     -    Modules and Imoprts
#=========================================================================
import math
math.sqrt(16) # 4.0

from math import sqrt, pi
sqrt(16) # 4.0

import math as m
sqrt(16) # 4.0

from math import * # avoid - pollutes namespace, hides where names came from
# my_module.py
def greet():
    print ('hello')

if __name__ == '__main__':
    # runs this when file is imported dir not when this is imported
    greet()
#=========================================================================
#           Day -07     -    File I/O
#=========================================================================
with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    # or: for line in f:.................

with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('Hello\n')
#=========================================================================
#           Day -07     -    Exception Handling
#=========================================================================
try:
    value = int(input('Enter a number: '))
except ValueError:
    print("That was not a valid number.")
except (TypeError, KeyError) as e:
    print(f' Something else wrong: {e}')
else:
    print('ran only if no exception occured.')
finally:
    print('always runs - cleanup code goes here.')
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

class InsufficientFundsError(Exception):
    pass
