# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# In Python sets are written with curly brackets.

# Example
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so the items will appear in a random order.
# Note: Sets are unindexed, so you cannot access items in a set by referring to an index,
# since sets have no index.

# The values True and False are the only two boolean values and they are the same as 1 and 0.
# You can evaluate any expression in Python, and get one of two answers, True or False.

# Example
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

## Subsections: access items, change items, add items, remove items, loop sets,

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Note: You cannot change items in a set, but you can add new items.
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# You can also use the update() method to add items from any iterable (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Remove Items
thisset.remove("banana")

print(thisset)

## Subsections: union, intersection, symmetric difference

'''
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Or use the pipe | operator that works for sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

# & operator that works for sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

## Subsections: Frozen Sets

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
