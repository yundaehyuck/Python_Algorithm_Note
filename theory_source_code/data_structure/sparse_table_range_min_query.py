import math
from sys import stdin

#sparse table, range min query basic

def sparse_table(A):
    
    k = int(math.log2(n))
    
    #st[i][j] = 구간 [j, j+2^i-1]에 대한 정답
    st = [[0]*n for _ in range(k+1)]
    
    #i = 0인 경우는 원래 배열 A와 동일하다.
    for i in range(n):
    
        st[0][i] = A[i]
    
    #구간의 길이를 절반으로 나눠서, 이전에 구한 답들을 이용하여
    #다이나믹 프로그래밍을 이용해 sparse table을 채워넣는다.
    for i in range(1,k+1):
    
        j = 0

        while j + (1 << i) - 1 < n:
        
        #st[i][j] = [j,j+2^i-1] = [j,j+2^(i-1)-1] + [j+2^(i-1),j+2^i-1]

        #st[i-1][j] = [j,j+2^(i-1)-1] 

        #st[i-1][j+1<<(i-1)] = [j+2^(i-1),(j+2^(i-1))+2^(i-1)-1] = [j+2^(i-1), j+2^i-1]
        
            st[i][j] = min(st[i-1][j], st[i-1][j+(1<<(i-1))])

            j += 1
    
    return st

#range min query에 답을 하는 방법

#[l,r]에서 최솟값 min([l,r])은 어떤 길이 2^i인 두 구간 
#min([l,l+2^i-1], [r-2^i+1,r])에서 최솟값과 동일하다.

#i = log2(r-l+1)

def min_query(a,b):
    
    k = int(math.log2((b - a + 1)))
    
    return min(st[k][a-1],st[k][b-1-(1<<k)+1])
    
n,m = map(int,stdin.readline().split())

A = [int(stdin.readline()) for _ in range(n)]

st = sparse_table(A)

for _ in range(m):
    
    a,b = map(int,stdin.readline().split())
    
    print(min_query(a,b))