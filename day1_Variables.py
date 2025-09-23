x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Assign multiple values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assign the same value to multiple variables in one line
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Concatenate variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# "+" is used to concatenate variables
# "," is used to add a space between variables
# "+" works as the mathematical addition operator if the variables are numbers
x = 5
y = 10
print(x + y)

# "+" cannot be used to concatenate a string and a number
x = 5
y = "John"
#print(x + y) # This will produce an error

# But we can use "," to separate them
print(x, y)

# Global variables
x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc()

# Global variables
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global x 
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)