from math import *
n = int(input())
a = int(input())
p = n*a
re = radians(180/n)
apofema = a/(2*tan(re))
print(apofema*p/2)