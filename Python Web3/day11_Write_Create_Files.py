
'''
"a" append - will append to the end of the file
"w" write - will overwrite any existing file or create a new file if it doesn't exist
"t" text - will read/write text files
"b" binary - will read/write binary files

'''

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())

# Create a new file
f = open("myfile.txt", "x")


