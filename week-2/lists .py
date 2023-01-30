thislist = ["apple", "banana", "cherry"]
print(thislist)
#
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)