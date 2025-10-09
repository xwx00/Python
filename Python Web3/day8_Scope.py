'''
A variable is only available from inside the region it is created. This is called scope.
'''

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


# Nonlocal keyword
# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())