def nCr(n,r,s):

    if r == 0: ##모든 자리를 채우면

        print(*comb)
    
    else:

        for i in range(s,n-r+1):

            comb[r-1] = A[i] ##r-1번째에 A[i]를 채워넣고

            nCr(n,r-1,i+1) ##다음 자리에는 i+1~부터 사용하도록


A = [1,2,3,4,5]

n = len(A)

r = 3

comb = [0] * r

nCr(n,r,0)

"""
3 2 1
4 2 1
5 2 1
4 3 1
5 3 1
5 4 1
4 3 2
5 3 2
5 4 2
5 4 3
"""