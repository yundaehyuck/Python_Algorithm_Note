def bfs(v,N): #시작정점 v, 마지막 정점 N
    
    #visited 생성

    visited = [0] * (N+1)

    #큐를 생성함

    q = [] 

    q.append(v) #시작점이 들어간 큐
    ### q=[v] 

    visited[v] = 1

    while q: #큐가 비어있지 않다면 탐색
        
        v = q.pop(0) #시작점 뽑아내기

        #방문한 v를 이용해 할일
        print(v)

        #인접하고 미방문한 (in queue되지 않은) 정점 w가 있으면...

        for w in adjList[v]: #v에 인접한 정점 w에 대하여
            
            if visited[w] == 0: #방문한 적이 없는 정점이라면..
                
                q.append(w)
                visited[w] = 1