# Built-In Functions/Modules

import random, sys, os, math
from random import *
import sys

random.randint(1,10)
randint(1,10)
sys.exit()

# Third Party Modules - use pip
# In command line, type cd "Program Files\Python 3.5\Scripts"
# In command line, type pip.exe install moduleName
# In command line, type exit

# Writing Your Own Functions

def hello():
  print("Howdy")

hello()

def plusOne(number):
    return number + 1

number = plusOne(5)
print(number)

print('Cat','dog','mouse',sep='ABC')


total_eggs = 0 # global variable

def BeatEggs():
    eggs_native = 10
    eggs_imported = 1
    total_eggs_toBeat = eggs_native + eggs_imported
    # print('total eggs to beat: ' + str(total_eggs_toBeat))
    return total_eggs_toBeat

total_eggs = BeatEggs()
print('Eggs to beat: ' + str(total_eggs))

def divBy(numberToDiv,dividyBy):
  try:
    return numberToDiv/dividyBy
  except ZeroDivisionError:
    print("Cannot divide by 0")

# except can have no argument

print(divBy(1,0))

print("how many cats do you have?")
numCats = input()
try:
  if int(numCats) >=4:
    print("A lot of cats")
  else:
    print("not a lot of cats")
except ValueError:
  print("Should be numerical")
  

