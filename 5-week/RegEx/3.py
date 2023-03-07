import re
strer = input()
rex = re.search('^[a-z]+_[a-z]+$', strer)
if rex:
    print('Yes')
else:
    print('No')