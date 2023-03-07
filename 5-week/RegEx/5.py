import re
strer = input()
rex = re.search('a*b$', strer)
if rex:
    print('Yes')
else:
    print('No')