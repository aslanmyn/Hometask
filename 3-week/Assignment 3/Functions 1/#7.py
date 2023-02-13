def has33(listok):
    d = 0
    for i in range(1,len(listok)):
        if listok[i] == 3 and listok[i-1] == 3:
            d = d+1
    if d > 0:
        print('True')
    else:
        print('False')
has33([1, 3, 3])
has33([1, 3, 1, 3])
has33([3, 1, 3])
# True
# False
# False