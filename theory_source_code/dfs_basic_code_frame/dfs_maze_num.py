visited = [[0]*N for _ in range(N)]

def dfs(i,j,N):

    global answer
    
    if maze[i][j] == 3:
        
        answer += 1
        
        return
    
    else:
        
        visited[i][j] = 1
        
        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            
            ni,nj = i+di,j+dj 

            if (ni >= 0 and ni <= N-1) and (nj >= 0 and nj <= N-1) and maze[ni][nj] != 1 and visited[ni][nj] == 0: 
                dfs(ni,nj,N)
                visited[ni][nj] = 0
        
        #visited[i][j] = 0 #다른 경로에서 i,j 경로를 들어온다면, 통과하도록 만들어준다..???
        
        return
    
answer = 0

dfs(s,g,N)

print(answer)