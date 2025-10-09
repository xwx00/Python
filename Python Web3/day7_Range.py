# Syntax for using range()
for i in range(5):  # 0 to 4
    print(i)

# range(start, stop, step)
x = range(3, 10, 2)
for i in x:
    print(i)


print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))