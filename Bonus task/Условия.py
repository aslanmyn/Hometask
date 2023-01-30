# 1
a = int(input())
b = int(input())
if a<b :
  print(a)
else:
  print(b)

# 2
a = int(input())
if a>0:
    print('1')
elif a==0:
    print('0')
else:
    print('-1')

# 3
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a+b)%2 ==(c+d)%2:
    print('YES')
else:
    print('NO')

# 4
a = int(input())
if a%4==0 and a%100 !=0 or a%400 == 0:
    print('YES')
else:
    print('NO')

# 5
a = int(input())
b = int(input())
c = int(input())
print(min(a,b,c))

# 6
a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print('3')
elif a==b or a==c or c==b:
    print('2')
else:
    print('0')

# 7
a =int(input())
b =int(input())
c =int(input())
d =int(input())
if a ==c or b ==d :
    print('YES')
else:
    print('NO')

# 8
a =int(input())
b =int(input())
c =int(input())
d =int(input())
if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print('YES')
else:
    print('NO')

# 9
a,b,c,d =int(input()),int(input()),int(input()),int(input())
if  abs(a-c)==abs(b-d):
    print('YES')
else :
    print('NO')

# 10
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
# 11
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if (abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(y1-y2)==2 and abs(x1-x2)==1):
    print('YES')
else:
    print('NO') 
# 12
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')

# 13
n = int(input())
m = int(input())
x = int(input())
y = int(input())


if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
  
if x < y:
    print(x)
else:
    print(y)