'''
F-Strings (Formatted String Literals)
F-strings, introduced in Python 3.6, provide a way to embed expressions inside string literals, using curly braces {}. They are prefixed with 'f' or 'F'.
'''

name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.


txt = f"The price is {95:.2f} dollars"
print(txt)

# Perform calculations inside the curly braces
txt = f"The price is {20 * 59} dollars"
print(txt)

# Use commas as thousand separators
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)  # Output: The price is 59,000 dollars