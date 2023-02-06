#1
a = input()
print(a[2])
print(a[len(a)-2])
print(a[:5])
print(a[:len(a)-2])
print(a[: :2])
print(a[1: :2])
print(a[: :-1])
print(a[: :-2])
print(len(a))

#2
a = input()
print(a.count(' ')+1)
#3
a = input()
print(a[len(a)//2+len(a)%2:],end='')
print(a[:len(a)//2+len(a)%2])
#4
a =input()
print(a[a.find(' ')+1:],end=' ')
print(a[:a.find(' ')])

# 5
a = input()
if a.count('f')>1:
        print(a.find('f'))
        print(a.rfind('f'))
elif a.find('f') ==-1:
    print('')
else:
    print(a.find('f'))
# 6
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
# 7
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)
# 8
s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)
# 9
a = input()
print(a.replace('1','one'))
# 10
a =input()
print(a.replace('@',''))
#11
s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)
#12
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)
