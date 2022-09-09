def bfs(v,N,t): #시작정점 v, 마지막 정점 번호 N, 도착하고자 하는 정점 t
    
    visited = [0] * (N+1)

    q - []

    q.append(v) 

    visited[v] = 1

    while q:
        
        v = q.pop(0)

        ##내가 찾고자하는 목표인지 확인하는게 이 문제의 목적

        if v == t:
            
            return 1 #목표를 찾음
        
        for w in adjList[v]:
            
            if visited[w] == 0:
                
                q.append(w)
                visited[w] = visited[v] + 1