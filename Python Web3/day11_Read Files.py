open("demofile.txt","w").write("Hello World!\nWelcome to Python File Handling.")


f = open("demofile.txt")
print(f.read())


# With statement
with open("demofile.txt") as f:
  print(f.read())

f = open("demofile.txt")
print(f.readline())
f.close()

# Read lines
with open("demofile.txt") as f:
  for x in f:
    print(x)