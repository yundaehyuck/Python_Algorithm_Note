def permutation_with_repetition(i,r):

    if i == r:

        print(p)
    
    else:

        for j in range(r):

            p[i] = a[j]

            permutation_with_repetition(i+1,r)


n = 3

a = [i for i in range(1,n+1)]

p = [0]*n

permutation_with_repetition(0,n)

"""
[1, 1, 1]
[1, 1, 2]
[1, 1, 3]
[1, 2, 1]
[1, 2, 2]
[1, 2, 3]
[1, 3, 1]
[1, 3, 2]
[1, 3, 3]
[2, 1, 1]
[2, 1, 2]
[2, 1, 3]
[2, 2, 1]
[2, 2, 2]
[2, 2, 3]
[2, 3, 1]
[2, 3, 2]
[2, 3, 3]
[3, 1, 1]
[3, 1, 2]
[3, 1, 3]
[3, 2, 1]
[3, 2, 2]
[3, 2, 3]
[3, 3, 1]
[3, 3, 2]
[3, 3, 3]
"""