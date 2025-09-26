a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

bool(False)

bool(None)

bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

s = 'First line.\nSecond line.'
print(s)

word = 'Python'

print(word[-2:]+word[:2])    # Last two characters
print(word[2:]+word[:2])  