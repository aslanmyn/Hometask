with open('termo.py', 'r') as input_file:
    file_contents = input_file.read()

with open('torretto.py', 'w') as output_file:
    output_file.write(file_contents)