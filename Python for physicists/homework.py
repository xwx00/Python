import math as mt

x = 20
while x < 100:
    x = x*mt.fabs(-1/2)
    x = x / (-(-1/2)**2)
    print(x)