# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.
# Example

# Subsections: Python Dictionaries
from os import name


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Subsections: access items, change items, add items, remove items, loop dictionaries
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

# Add a new item to the original dictionary, and see that the keys list gets updated as well.
car["color"] = "white"
print(x) #after the change

x = thisdict.values()

print(x)

# The items() method will return each item in a dictionary, as a list of tuples.
x = thisdict.items()
print(x) 

# Delete the "model" item from the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

for x in thisdict.keys():
  print(x)


## Subsections: nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1Info = myfamily["child1"]
print(child1Info)

child1Name = myfamily["child1"]["name"]
print(child1Name)


# loop through the nested dictionary, and print the name and year of each child:
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


for x, obj in myfamily.items():
  print(myfamily[x])
  print(obj)


# More readable nested iteration with clearer variable names
for child_key, child_data in myfamily.items():
    print(f"Child: {child_key}")
    for attribute, value in child_data.items():
        print(f"  {attribute}: {value}")
    print()  # Empty line for readability