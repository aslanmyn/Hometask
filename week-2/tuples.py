thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# 
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
# 
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
 
#
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
