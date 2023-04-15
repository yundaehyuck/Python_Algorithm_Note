#boj 1238

import heapq
from sys import stdin

def dijkstra(start,graph):
    
    q = []

    heapq.heappush(q,(0,start))

    INF = 1000000000000000000000

    distance = [INF]*(n+1)

    distance[start] = 0

    while q:
        
        dist,u = heapq.heappop(q)

        if distance[u] < dist:
            
            continue
        
        for b,c in graph[u]:
            
            cost = dist+c

            if cost < distance[b]:
                
                distance[b] = cost

                heapq.heappush(q,(cost,b))
    
    return distance


n,m,x = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)]

inverse_graph = [[] for _ in range(n+1)]

for _ in range(m):
    
    a,b,c = map(int,stdin.readline().split())

    graph[a].append((b,c))
    inverse_graph[b].append((a,c)) ##역방향 그래프를 만들어준다.


distance_outcome = dijkstra(x,graph) #dist[i] = x번 정점에서 나머지 정점(i)으로 가는 최단 경로
distance_income = dijkstra(x,inverse_graph) #dist[i] = 나머지 정점(i)에서, x번 정점으로 되돌아오는 최단 경로

ans = 0

for i in range(1,n+1):

    cost = distance_income[i] + distance_outcome[i]

    if ans < cost:
        
        ans = cost


print(ans)