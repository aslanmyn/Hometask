my_list = ['Abu', 'Aru', 'Aslan', 'Syla']

with open('termo.py', 'w') as file:
    for item in my_list:
        file.write("%s\n" % item)