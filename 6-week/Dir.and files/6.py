import string
alphabet = string.ascii_uppercase
file_names = [f"{termo}.py" for termo in alphabet]
for file_name in file_names:
    with open(file_name, "w") as f:
        pass