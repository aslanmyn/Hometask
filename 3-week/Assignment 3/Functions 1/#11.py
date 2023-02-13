def poli(nemsbi):
    cwer = 0
    for i in range(0,len(nemsbi)//2):
        if nemsbi[i] ==nemsbi[len(nemsbi)-i-1]:
            cwer =cwer+1
    if cwer ==len(nemsbi)//2:
        print('YES')
    else:
        print('NO')
poli('madam')
# YES