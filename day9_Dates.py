'''
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
'''

import datetime
x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

# Create a date object
y = datetime.datetime(2025,10,1)

print(y)

print(y.strftime("%B"))