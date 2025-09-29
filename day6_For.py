# Example of a for loop with a break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Example of a for loop with a continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# Example of a for loop with an else statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
else:
  print("No more fruits")

for x in range(2, 30, 3):
  print(x)