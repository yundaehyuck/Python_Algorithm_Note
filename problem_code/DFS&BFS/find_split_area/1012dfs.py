# https://www.acmicpc.net/problem/1012
from sys import stdin,setrecursionlimit

setrecursionlimit(10000)

def dfs(x,y,n,m,square):
    
    if x < 0 or x > m-1 or y < 0 or y > n-1:
        
        return False
    
    if square[y][x] == 1:
        
        square[y][x] = 0

        dfs(x+1,y,n,m,square)
        dfs(x,y+1,n,m,square)
        dfs(x-1,y,n,m,square)
        dfs(x,y-1,n,m,square)
        return True
    
    return False




T = int(stdin.readline())

for _ in range(T):
    
    m,n,k = map(int,stdin.readline().split())

    square = [[0]*m for _ in range(n)]

    for _ in range(k):
        
        x,y = map(int,stdin.readline().split())

        square[y][x] = 1
    
    ans = 0

    for y in range(n):
        
        for x in range(m):
            
            ans += dfs(x,y,n,m,square)
    
    print(ans)