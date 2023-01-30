# 1
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

# 2
b = int(input())
h = int(input())
print(0.5 * b*h)
# 3
n = int(input())
k = int(input())

print(k//n)
print(k%n)

# 4
a=int(input())
if a>=60*24:
    a=a-(a//(60*24))*(60*24)
print(a//60)
print(a%60)

# 5
a = input()
print('Hello, ',a,'!',sep ='')

# 6
a = int(input())
print('The next number for the number',a,'is',a+1)
print('The previous number for the number',a,'is',a-1)

# 7
a=int(input())
b=int(input())
c=int(input())
print((a+1)//2 +(b+1)//2+(c+1)//2)

# 8
a = int(input())
b = int(input())
L = int(input())
N = int(input())
print(2 * L + (2 * N - 1) * a + 2 * (N - 1) * b)
