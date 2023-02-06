#1
a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i)

#2
a = int(input())
b = int(input())
if a<=b:
    for i in range(a,b+1):
        print(i)
else:
    for j in range(a,b-1,-1):
        print(j)
# 3
a= int(input())
b= int(input())
for i in range(a,b-1,-1):
    if i %2 !=0:
        print(i)
# 4
sum = 0
for i in range(10):
    a = int(input())
    sum =sum +a
    
print(sum)
# 5
a = int(input())
sum = 0
for i in range(a):
    b = int(input())
    sum = sum + b
print(sum)

# 6
a = int(input())
sum = 0
for i in range(1,a+1):
    sum = sum +i**3
print(sum)

# 7
a = int(input())
sum = 1
for i in range(1,a+1):
    sum = sum*i
print(sum)

# 8
n = int(input())
factorial = 1
sum = 0
for i in range(1, n + 1):
    factorial *= i
    sum += factorial
print(sum)
# 9
a = int(input())
sum =0
for i in range(1,a+1):
    s = int(input())
    if s==0:
        sum+=1
print(sum)
# 10
a = int(input())
sum = ''
for i in range(1,a+1):
    sum =sum +str(i)
    print(sum)
# 11
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i

for i in range(n - 1):
    sum -= int(input())
print(sum)
# 

