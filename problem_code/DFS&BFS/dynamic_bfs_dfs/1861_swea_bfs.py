from collections import deque

def bfs(x,y,n,maps,visited):

    queue = deque([(x,y,1)])
    
    start = maps[y][x]

    max_distance = 0

    while queue:
        
        x,y,d = queue.popleft()

        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            
            dx = x + ni
            dy = y + nj

            if dx >= 0 and dx <= n-1 and dy >= 0 and dy <= n-1 and (maps[dy][dx] == maps[y][x] + 1):
                
                queue.append((dx,dy,d+1))
                    
                max_distance = d+1
                
                visited[dy][dx] = 1
                    
    return start,max_distance,visited
                
T = int(input())

for t in range(1,T+1):

    n = int(input())

    maps = [list(map(int,input().split())) for _ in range(n)]
    
    visited = [[0]*n for _ in range(n)]

    max_distance = 0

    min_start = n*n+1

    for y in range(n):
        
        for x in range(n):
            
            if not visited[y][x]:
                
                visited[y][x] = 1
            
                start,distance,visited = bfs(x,y,n,maps,visited)

                if max_distance < distance:

                    max_distance = distance
                    min_start = start

                elif max_distance == distance:

                    if min_start > start:

                        min_start = start
     
    print('#'+str(t),*[min_start,max_distance])