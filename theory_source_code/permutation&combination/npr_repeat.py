def nPr_repetition(i,n,r):

    if i == r:

        print(p)
    
    else:

        for j in range(n):

            p[i] = a[j]

            nPr_repetition(i+1,n,r)

n = 4

r = 2

a = [i for i in range(1,n+1)]

p = [0] * r

nPr_repetition(0,n,r)

"""
[1, 1]
[1, 2]
[1, 3]
[1, 4]
[2, 1]
[2, 2]
[2, 3]
[2, 4]
[3, 1]
[3, 2]
[3, 3]
[3, 4]
[4, 1]
[4, 2]
[4, 3]
[4, 4]
"""