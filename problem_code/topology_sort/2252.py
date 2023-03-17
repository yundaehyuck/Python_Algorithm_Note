from collections import deque
from sys import stdin

n,m = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)]

indegree = [0]*(n+1)

for _ in range(m):
    
    u,v = map(int,stdin.readline().split())

    graph[u].append(v)
    
    indegree[v] += 1


q = deque([])

for i in range(1,n+1):
    
    if indegree[i] == 0:
        
        q.append(i)

result = []

while q:
    
    now = q.popleft()

    result.append(now)

    for v in graph[now]:
        
        indegree[v] -= 1

        if indegree[v] == 0:
            
            q.append(v)

print(*result)