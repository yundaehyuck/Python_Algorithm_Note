#https://www.acmicpc.net/problem/2667

from collections import deque
from sys import stdin

def bfs(x,y,n,maps):
    
    queue = deque([(x,y)])

    cnt = 0

    if maps[y][x] == '0':
        
        return 0
    
    else:
        
        
        maps[y][x] = '0'
        
        cnt += 1
        
        while queue:
            
            x,y = queue.popleft()

            for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
                
                dx = x + ni
                dy = y + nj

                if dx >= 0 and dx <= n-1 and dy >= 0 and dy <= n-1 and maps[dy][dx] == '1':
                    
                    queue.append((dx,dy))
                    maps[dy][dx] = '0'
                    cnt += 1
            
        return cnt
                    

    

n = int(stdin.readline())

maps = [list(stdin.readline().rstrip()) for _ in range(n)]

cnt_list = []

ans = 0

for y in range(n):
    
    for x in range(n):
        
        cnt = bfs(x,y,n,maps)

        if cnt != 0:

            cnt_list.append(cnt)
            ans += 1

cnt_list.sort()

print(ans)

for cnt in cnt_list:
    
    print(cnt)