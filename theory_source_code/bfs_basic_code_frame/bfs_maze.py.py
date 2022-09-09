def bfs(i,j,N):
    
    visited = [[0]*N for _ in range(N)]

    q = []
    q.append((i,j))

    visited[i][j] = 1

    while q:
        
        i,j = q.pop(0)

        #도착지인가 아닌가?

        if maze[i][j] == 3:
            return 1
        
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]: #상하좌우 탐색
            
            ni,nj = i+di, j+dj

            if 0 <= ni and 0 <= nj and ni < N and nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                  
                  q.append((ni,nj))
                  visited[ni][nj] = visited[i][j] + 1 ##이렇게 하면 출발점에서 도착점까지의 최단거리를 알 수 있는?

    return 0