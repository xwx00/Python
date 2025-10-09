'''
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
'''

# An example of a Python function that can be used on different objects is the len() function.
# The len() function is used to return the length of an object, such as a string, list, tuple, etc.
# apply len() function to a string, it outputs the number of characters in the string:
x = "Hello World!"

print(len(x))
# apply len() function to a list, it outputs the number of items in the list:
y = [1, 2, 3, 4, 5]
print(len(y))
# apply len() function to a tuple, it outputs the number of items in the tuple:
z = (1, 2, 3)
print(len(z))

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive! "+self.brand+" "+self.model)

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail! "+self.brand+" "+self.model)

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly! "+self.brand+" "+self.model)

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()


# The move() method is used in all three classes, but it does different things depending on the object that calls it.
# This is Polymorphism, the method move() is the same but it acts differently on different classes.

# We can inherit from a parent class and override the move() method in the child classes:
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self): # Override the move() method of the Vehicle class
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object



for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()