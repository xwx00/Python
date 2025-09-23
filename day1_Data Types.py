'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list [], tuple (), range
Mapping Type:	dict {}
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

'''

# Examples
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# Get the data type
print(type("Hello"))
print(type(20))
print(type(20.5))
print(type(1j))
print(type(["apple", "banana", "cherry"]))
print(type(("apple", "banana", "cherry")))
print(type(range(6)))   
print(type({"name" : "John", "age" : 36}))
print(type({"apple", "banana", "cherry"}))  
print(type(frozenset({"apple", "banana", "cherry"})))
print(type(True))
print(type(b"Hello"))
print(type(bytearray(5)))
print(type(memoryview(bytearray(5))))
print(type(None))
print(type(x))