def slovo(listok):
    lister = listok.split()
    lister.sort(reverse = True)
    for x in lister:
        print(x,end=' ')
slovo('We are ready')
# ready are We