#
myset = {"apple", "banana", "cherry"}
#
thisset = {"apple", "banana", "cherry"}
print(thisset)
# 
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# 
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
# 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
# 
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# 
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
# 
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
# 
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
# 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
# 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
# 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)





