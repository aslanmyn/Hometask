import datetime

x = datetime.datetime.now()

a = (x.year) *31536000
b = (x.month) *604800
c = (x.day) *86400
d = (x.hour) *3600
e = (x.minute) *60
f = (x.second)
g = (x.microsecond)*0.000001
sum = a+b+c+d+e+f+g


x2 = datetime.datetime(2018, 6, 1)

a2 = (x2.year) *31536000
b2 = (x2.month) *604800
c2 = (x2.day) *86400
d2 = (x2.hour) *3600
e2 = (x2.minute) *60
f2 = (x2.second)
g2 = (x2.microsecond)*0.000001
sum2 = a2+b2+c2+d2+e2+f2+g2
print(sum -sum2)