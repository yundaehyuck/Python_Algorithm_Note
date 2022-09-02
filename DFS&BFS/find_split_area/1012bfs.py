# https://www.acmicpc.net/problem/1012

from collections import deque
from sys import stdin

def bfs(x,y,maps,n,m):

    queue = deque([(x,y)])

    if maps[y][x] == 1:
        
        maps[y][x] = 0

        while queue:
            
            x,y = queue.popleft()

            for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
                
                dx = x + ni
                dy = y + nj

                if (dx >= 0 and dx <= m-1) and (dy >= 0 and dy <= n-1) and maps[dy][dx] != 0:
                    
                    queue.append((dx,dy))
                    maps[dy][dx] = 0
             
   
        return 1

    else:
        
        return 0
    

T = int(stdin.readline())

for _ in range(1,T+1):
    
    m,n,k = map(int,stdin.readline().split())

    maps = [[0]*m for _ in range(n)]

    for _ in range(k):
        
        x,y = map(int,input().split())

        maps[y][x] = 1
    
    ans = 0

    for y in range(n):
        
        for x in range(m):
            
            ans += bfs(x,y,maps,n,m)
    
    print(ans)