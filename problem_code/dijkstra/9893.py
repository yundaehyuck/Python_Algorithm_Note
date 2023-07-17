import heapq
from sys import stdin

INF = 100000000000000000000000000000000000

m,n = map(int,stdin.readline().split())

graph = [[] * (m) for _ in range(m)]

for _ in range(n):
    
    u,v,c = map(int,stdin.readline().split())

    graph[u].append((v,c))

queue = []

distance = [(INF,INF) for _ in range(m+1)]

distance[0] = (0,0)

heapq.heappush(queue,(0,0,0))

while queue:
    
    count,dist,v = heapq.heappop(queue)

    if distance[v][0] < count:
        
        continue
    
    for u,c in graph[v]:
        
        cost = dist + c

        if distance[u][0] > count+1:
                
            distance[u] = (count+1,cost)

            heapq.heappush(queue,(count+1,cost,u))
        
        elif distance[u][0] == count+1:
            
            if distance[u][1] > cost:
                
                distance[u] = (count+1,cost)

                heapq.heappush(queue,(count+1,cost,u))

print(distance[1][1])