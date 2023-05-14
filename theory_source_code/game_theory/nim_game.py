from sys import stdin

n = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

z = A[0]

for i in range(1,n):
    
    z ^= A[i]

if z == 0:
    
    print('cubelover')

else:
    
    print('koosaga')