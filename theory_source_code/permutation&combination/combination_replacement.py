def nHr(n,r,s):

    if r == 0:

        print(*comb)
    
    else:

        for i in range(s,n):

            comb[r-1] = A[i]

            nHr(n,r-1,i)

A = [1,2,3,4,5]

n = len(A)

r = 3

comb = [0] * r

nHr(n,r,0)

"""
1 1 1
2 1 1
3 1 1
4 1 1
5 1 1
2 2 1
3 2 1
4 2 1
5 2 1
3 3 1
4 3 1
5 3 1
4 4 1
5 4 1
5 5 1
2 2 2
3 2 2
4 2 2
5 2 2
3 3 2
4 3 2
5 3 2
4 4 2
5 4 2
5 5 2
3 3 3
4 3 3
5 3 3
4 4 3
5 4 3
5 5 3
4 4 4
5 4 4
5 5 4
5 5 5
"""