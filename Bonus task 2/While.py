#1
a = int(input())
i =1
while i**2 <=a:
    print(i**2)
    i=i+1
# 2
a = int(input())
i = 1
while a>i:
    i+=1
    if a%i ==0:
        print(i)
        break

# 3
number = int(input())
i = 1
while 2**i <= number:
    i += 1
print(i-1, 2**(i-1))
# 4
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)
# 5
len = 0
while int(input()) != 0:
    len += 1
print(len)

# 6
a = int(input())
c=a

while a!=0:
    a = int(input())
    c=c+a
print(c)
# 7
sum = 0
len = 0
element = int(input())
while element != 0:
    sum += element
    len += 1
    element = int(input())
print(sum / len)
# 8
max = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
print(max)

# 9
max = 0
index_of_max = -1
element = -1
len = 0
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)
# 10
su = 0
a = int(input())
while a!= 0:
    
    if a%2==0 and a!=0:
        su+=1
    a = int(input())    
print(su)

# 11
prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)
# 12
max1=0
max2=0
a=int(input())
while a != 0:
    if a>max1:
        max2=max1
        max1=a
    elif a>max2 :
        max2=a
    a=int(input())
print(max2)
# 13
maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1        
print(num_maximal)
# 14
n = int(input())
a, b = 1, 1
if n ==0:
    print('0')
else:
    for i in range(n-1):
        a, b = b, a + b
    print(a)
# 15
x=0
x1=1
x2=0
i=0
n=int(input())
while x<=n:
    x=x1+x2
    x1,x2=x,x1
    i+=1
if (n==x2):
    print(i)
else:
    print(-1)
# 16
prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)
# 17
x = int(input())
n = []
while x != 0:
    n.append(x)
    x = int(input())
    
M = sum(n)/len(n)
STD = 0
for i in n:
    STD += (i-M)**2
STD = ( STD/(len(n)-1) )**0.5
print(STD)
