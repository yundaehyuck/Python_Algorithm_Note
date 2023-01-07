import heapq
from sys import stdin

INF = 100000000000000000000000000000

def dijkstra(start,n):
    
    q = []

    distance = [[INF,INF] for _ in range(n+1)]

    distance[start][0] = 0
    distance[start][1] = 0

    heapq.heappush(q,(0,start))

    while q:
        
        dist,v = heapq.heappop(q)
    
        if distance[v][dist%2] < dist:

             continue

        for b,c in graph[v]:

            cost = dist + c

            if distance[b][cost%2] > cost:

                distance[b][cost%2] = cost
                heapq.heappush(q,(cost,b))
    
    return distance

n,m = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    
    a,b,c = map(int,stdin.readline().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

distance = dijkstra(1,n)

if distance[n][1] == INF:
    
    print(0)

else:
    
    print(distance[n][1])