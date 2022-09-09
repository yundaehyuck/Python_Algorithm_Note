#https://www.acmicpc.net/problem/7562
from collections import deque
from sys import stdin

def bfs(x,y,s,g,n,maps):
    
    queue = deque([(x,y)])

    if x == s and y == g:
        
        return maps[y][x]
    
    else:
        
        maps[y][x] = 1

        delta = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]

        while queue:
            
            x,y = queue.popleft()

            for ni,nj in delta:
                
                dx = x + ni
                dy = y + nj

                if dx >= 0 and dx <= n-1 and dy >= 0 and dy <= n-1 and maps[dy][dx] == 0:
                    
                    queue.append((dx,dy))
                    maps[dy][dx] = maps[y][x] + 1

                    if dx == s and dy == g:
                        
                        return maps[dy][dx]-1
        

    
    
T = int(input())

for _ in range(1,T+1):
    
    n = int(stdin.readline())

    maps = [[0]*n for _ in range(n)]

    x,y = map(int,stdin.readline().split())

    a,b = map(int,stdin.readline().split())

    print(bfs(x,y,a,b,n,maps))