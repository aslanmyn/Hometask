
import re
strer = input()
rex = re.search('[A-Z]{1}[a-z]', strer)
if rex:
    print('Yes')
else:
    print('No')