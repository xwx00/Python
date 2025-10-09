'''
A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
'''

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# Multiple Decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner
print("1st decorator")

def addgreeting(func):
  def myinner():
    print("2nd decorator")
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())


@addgreeting
@changecase
def myfunction2():
  return "Tobias"

print(myfunction2())