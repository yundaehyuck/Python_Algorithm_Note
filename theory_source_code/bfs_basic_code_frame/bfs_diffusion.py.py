def bfs(i,j,N,visited):
    

    queue = [(i,j)]

    visited[i][j] = 1
    day = 0

    while queue:

        size = len(queue)

        print(f'{day}일차')
        print('############')

        for k in range(n):
            
            print(visited[k])
        
        print('############')

        for _ in range(size):

            i,j = queue.pop(0)

            for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                
                ni = i + di
                nj = j + dj

                if (ni >= 0 and ni <= N-1) and (nj >= 0 and nj <= N-1) and visited[ni][nj] == 0:
                    
                    queue.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1
        
        day += 1


N = 10

visited = [[0]*N for _ in range(N)]

print(bfs(5,5,10,visited))