import re
strer = input()
rex = re.sub(r"(\w)([A-Z])", r"\1 \2", strer)
print(rex)