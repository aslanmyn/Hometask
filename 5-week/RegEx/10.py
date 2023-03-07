import re
strer = input()
rex = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', strer)
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', strer).lower())