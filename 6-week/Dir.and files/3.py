import os

path = r"C:\Users\User\Desktop\6-week\Dir.and files"

if os.path.exists(path):
    directory = os.path.dirname(path)
    filename = os.path.basename(path)

    print(f"Path exists at {path}")
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
else:
    print(f"Path {path} does not exist")
