'''
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
'''

import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

# Rename module name

import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in Modules
import platform

x = platform.system()
print(x)

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x)

# Import only parts from a module
from mymodule import person1
print (person1["age"])
