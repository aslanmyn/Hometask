def filter_prime(listok):
    for i in listok:
        k = 0
        for j in range(2,len(listok)+1):
            if (i % j == 0):
                k = k + 1
        if (k <= 1):
            print(i,)

filter_prime([2,3,4,5,6,7,8,1,13])
# 2 3 5 7 1 13