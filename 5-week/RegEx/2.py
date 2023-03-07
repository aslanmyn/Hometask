import re
strer = input()
rex = re.search(r'ab{2}|b{3}', strer)
if rex:
    print('Yes')
else:
    print('No')