def solve(numheads, numlegs):
    for i in range(1,94):
        for j in range(1,94):
            if 4*i + 2*j == numheads and i + j == numlegs:
                print(i,j)

solve(94,35)