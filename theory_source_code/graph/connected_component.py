from collections import deque
from sys import stdin

def bfs(x,n,visited,graph):
    
    queue = deque([x])

    visited[x] = 1

    while queue:
        
        x = queue.popleft()

        for v in graph[x]:
            
            if visited[v] == 0:
                
                visited[v] = 1
                queue.append(v)
    
    return True


n,m = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    
    u,v = map(int,stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)

count = 0

for i in range(1,n+1):
    
    if visited[i] == 0:
        
        count += bfs(i,n,visited,graph)

print(count)