#다익스트라를 이용한 minimum bottleneck path 알고리즘

import heapq
from sys import stdin

INF = 10000000000000000000000000

def dijkstra(start):
    
    queue = []

    heapq.heappush(queue,(0,start))

    distance = [INF]*(n+1) #"정점 i로 도착하는 동안 탐색한 최대 가중치의 최솟값"

    distance[start] = 0

    while queue:
        
        h,u = heapq.heappop(queue)

        if distance[u] != h:
            
            continue
        
        for v,c in graph[u]:
            
            cost = max(h,c) #경로를 탐색하면서, cost는 경로 가중치가 최대인 값으로 갱신
            
            #최대 가중치의 최솟값이 더 작아진다면, 갱신해준다
            if  distance[v] > cost:

                distance[v] = cost
                heapq.heappush(queue,(cost,v))
    
    return distance

#boj 23286
n,m,t = map(int,stdin.readline().split())

graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    
    u,v,h = map(int,stdin.readline().split())

    graph[u].append((v,h))

#모든 정점에 대해 minimum bottleneck path를 구해놓은 배열을 미리 계산
dist = [0]

for i in range(1,n+1):
    
    dist.append(dijkstra(i))

#미리 계산해놓은 배열을 이용해 쿼리에 O(1)에 답해주기
for _ in range(t):
    
    u,v = map(int,stdin.readline().split())

    if dist[u][v] == INF:
        
        print(-1)
    
    else:
        
        print(dist[u][v])