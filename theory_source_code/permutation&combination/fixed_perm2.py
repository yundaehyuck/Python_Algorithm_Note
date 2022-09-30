def permutation(i,n,r,f):

    if i == r:

        print(p)
    
    else:

        for j in range(n):

            if i == f: ##i가 고정시킨 f라면..

                i = i + 1 #그냥 i에 1을 더해 그 자리는 건너 뛰도록

            if used[j] == 0:

                used[j] = 1

                p[i] = a[j]

                permutation(i+1,n,r,f)

                used[j] = 0

n = 5
r = 3

a = [i for i in range(1,n+1)]

used = [0] * n
p = [0] * r

##1번자리가 3인 길이가 3인 순열
p[1] = 3
used[2] = 1

permutation(0,n,r,1)

"""
[1, 3, 2]
[1, 3, 4]
[1, 3, 5]
[2, 3, 1]
[2, 3, 4]
[2, 3, 5]
[4, 3, 1]
[4, 3, 2]
[4, 3, 5]
[5, 3, 1]
[5, 3, 2]
[5, 3, 4]
"""