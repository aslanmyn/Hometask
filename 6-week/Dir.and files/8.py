
import os
path = r"C:\Users\User\Desktop\6-week\Dir.and files\termo.py"

if os.path.exists(path):
    os.remove(path)
else:
    print(f"Path {path} does not exist")