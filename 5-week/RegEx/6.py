import re
strer = input()
rex = re.sub("[ ,.]", ':', strer)
print(rex)