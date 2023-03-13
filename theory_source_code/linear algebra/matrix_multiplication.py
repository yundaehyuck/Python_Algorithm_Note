from sys import stdin

n,m = map(int,stdin.readline().split())

A = [list(map(int,stdin.readline().split())) for _ in range(n)]

m,k = map(int,stdin.readline().split())

B = [list(map(int,stdin.readline().split())) for _ in range(m)]

C = [[0]*k for _ in range(n)]

for i in range(n):
    
    for j in range(k):
        
        for w in range(m):
            
            C[i][j] += A[i][w]*B[w][j]

for row in C:
    
    print(*row)