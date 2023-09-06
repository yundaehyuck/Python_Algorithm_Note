#bidirectional BFS

from collections import deque
from sys import stdin

def bfs(s,graph):
    
    queue = deque([s])

    visited = [0]*(n+1)

    visited[s] = 1

    count = 0

    while queue:
        
        v = queue.popleft()

        for u in graph[v]:
            
            if visited[u] == 0:
                
                count += 1
                visited[u] = 1 #v에서 u로 도달 가능
                queue.append(u)
        
    return count
                
n = int(stdin.readline())

m = int(stdin.readline())

graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for _ in range(m):
    
    i,j = map(int,stdin.readline().split())

    graph1[i].append(j)
    graph2[j].append(i) #reverse graph

for i in range(1,n+1):
    
    #전체 n개에서 자기 자신 1개 빼고, 나머지 도달 가능한 정점 수 빼주면 도달 불가능한 정점 수
    print(n-1 - (bfs(i,graph1) + bfs(i,graph2)))