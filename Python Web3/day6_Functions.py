def my_function():
    print("Hello from a function")


my_function()

# Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Positional-Only Parameters
def my_function(x, /):
  print(x)

my_function(3)

# Without /, you are able to call the function like this:
def my_function(x):
  print(x)

my_function(x = 3)

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add before the arguments:*,
def my_function(*, x):
  print(x)

my_function(x = 3)

# combine different types of arguments
def my_function(a, b, /, *, c, d): # b is positional-only, c and d are keyword-only
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# Recursion function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

