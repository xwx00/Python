'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

  # The raise keyword is used to raise an exception.
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")