import datetime

x = datetime.datetime.now()

print(x.year,end=':')
print(x.month,end=':')
print(x.day-5,end=':')
print(x.hour,end=':')
print(x.minute,end=':')
print(x.second,end=':')
print(x.microsecond)