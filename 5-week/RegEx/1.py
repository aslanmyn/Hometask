import re
strer = input()
rex = re.findall(r'ab*', strer)
if rex:
    print('Yes')
else:
    print('No')