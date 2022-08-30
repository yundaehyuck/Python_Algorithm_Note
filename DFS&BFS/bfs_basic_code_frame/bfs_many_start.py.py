def bfs(N):
    visited = [[0]*N for _ in range(N)]

    q = []

    ##시작점을 모두 찾아서 탐색 시작

    for i in range(N):
        
        for j in range(N):
            
            if maze[i][j] == 2:
                
                q.append((i,j))
                visited[i][j] = 1
    
    while q:
        
        i,j = q.pop(0)

        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            
            ni,nj = i+di,j+dj 

            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0: #벽으로 둘러싸인 미래라서 범위 검사를 안함
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1

                ###if max_v < visited[i][j]:
                    ###max_v = visited[i][j] ##맥스값 갱신하거나, visited 순회해서 맥스값 찾거나