import re
strer = input()

print((''.join(x.capitalize() or '_' for x in strer.split('_'))))