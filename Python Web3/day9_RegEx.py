'''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

It can be used for string searching and manipulation tasks such as:
'''
import re

txt = "The rain in Spain"
x = re.search("ai", txt)

# RegEx Functions
# findall() - Returns a list containing all matches
# search() - Returns a Match object if there is a match anywhere in the string
# split() - Returns a list where the string has been split at each match
# sub() - Replaces one or many matches with a string


# Metacharacters
# [] - A set of characters
txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

# \ - Signals a special sequence (can also be used to escape special characters)

x = re.findall("\d", txt)
print(x)

# . - Any character (except newline character)

x = re.findall(".", txt)
print(x)

# ^ - Starts with
x = re.findall("^The", txt)
print(x)

# $ - Ends with
x = re.findall("Spain$", txt)
print(x)

txt2 = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt2)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

# * - Zero or more occurrences
txt3 = "The rain in Spain falls mainly in the plain!"
x = re.findall("ai.*", txt3)
print(x)

# + - One or more occurrences
x = re.findall("ai+", txt3)
print(x)

# ? - Zero or one occurrences
x = re.findall("ai?", txt3)
print(x)

# {} - Exactly the specified number of occurrences
x = re.findall("a{2}", txt3)
print(x)

# | - Either or
x = re.findall("falls|stays", txt3)
print(x)

# () - Capture and group
x = re.findall("(falls|in)", txt3)
print(x)


# Special Sequences
# \A - Returns a match if the specified characters are at the beginning of the string
x = re.findall("\AThe", txt3)
print(x)
# \b - Returns a match where the specified characters are at the beginning or at the end of a word
x = re.findall(r"\bain", txt3)
print(x)



# findall() - Returns a list containing all matches
x = re.findall("ai", txt3)
print(x)


# search() - Returns a Match object if there is a match anywhere in the string
x = re.search("falls", txt3)
print(x) #this will print an object

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)