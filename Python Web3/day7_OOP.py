'''
OOP stands for Object-Oriented Programming.

Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
'''

# Advantages of OOP:
# 1. Encapsulation: Bundling data and methods that operate on that data within a single unit (class).
# 2. Inheritance: Creating new classes based on existing ones, promoting code reuse.
# 3. Polymorphism: Allowing methods to do different things based on the object it is acting upon.
# 4. Abstraction: Hiding complex implementation details and exposing only the necessary parts.

# What are classes and objects?
# A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that the objects created from the class will have.
# An object is an instance of a class. It is created using the class blueprint and can have its own unique data.

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

# The __init__() Function
# The __init__() function is a special method that is called when an object is instantiated

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The _str_() Function
# The __str__() function is a special method that returns a string representation of the object. It is called by the str() built-in function and by the print statement.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# Modify objeect properties

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40

del p1.age

# print(p1.age) # This will raise an AttributeError since age has been deleted