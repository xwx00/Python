## SECTION 4: LISTS
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
myList = ["apple", "banana", "cherry"];
print(myList);

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist);
print(len(thislist));
print(thislist[1]);

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

## Subsection: Modify Lists
# change list item
thislist[1] = "blackcurrant"
print(thislist);


# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, 
# and refer to the range of index numbers where you want to insert the new values:

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# append item 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove the first item with the specified value:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove the specified index using the pop() method:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

## Subsection: Loop Lists
# loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

## Subsection: List Comprehension
# A list comprehension is a shorter syntax to create a new list based on the values of an existing list.
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in thislist if "a" in x]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

## Subsection: Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

## Subsection: Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

## Subsection: Join Lists
# To join two or more lists into one list, use the + operator.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)