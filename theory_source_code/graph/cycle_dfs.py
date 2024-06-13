def dfs(u):
    
    #u에서 dfs가 진행중인데 (visited[u] = -1 or 1)
    #u를 다시 방문하였음
    if visited[u]:
        
        #u에서 dfs가 아직 안끝났는데 u를 다시 방문하였다면
        #사이클이 존재함
        if visited[u] == -1:

            return True
        
        #이미 u에서 dfs가 끝난 상태이면 다른 노드에서 u로 온 것이다
        return False
    
    #u에서 dfs 시작
    visited[u] = -1

    for v in graph[u]:

        if dfs(v): #u와 인접한 경로를 이동하면서 방문
            
            return True #dfs가 True를 반환한 경우, 사이클이 존재한다는 의미
    
    #u에서 dfs가 끝났다는 의미
    visited[u] = 1

    #끝났는데도, 아직 True를 반환하지 못하면 사이클이 없음
    return False

n = 7

edges = [(4,1),(1,2),(2,3),(3,1),(5,3),(6,5),(7,5)]

graph = [[] for _ in range(n+1)]

for a,b in edges:
    
    graph[a].append(b)

visited = [0]*(n+1)

print(dfs(7))

True