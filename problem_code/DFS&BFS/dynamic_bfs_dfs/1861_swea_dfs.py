def dfs(x,y,n,d,maps,visited):
    
    global max_d
    
    visited[y][x] = 1

    for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
        
        dx = x + ni
        dy = y + nj

        if dx >= 0 and dx <= n-1 and dy >= 0 and dy <= n-1 and (maps[dy][dx] == maps[y][x] + 1):
            
            dfs(dx,dy,n,d+1,maps,visited)
    
    if max_d < d:
        
        max_d = d

    return max_d,visited
                
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
                
                start = maps[y][x]

                max_d = 0
                            
                distance,visited = dfs(x,y,n,1,maps,visited)

                if max_distance < distance:

                    max_distance = distance
                    min_start = start

                elif max_distance == distance:

                    if min_start > start:

                        min_start = start
     
    print('#'+str(t),*[min_start,max_distance])