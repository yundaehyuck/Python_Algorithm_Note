#boj 14221
import heapq
from sys import stdin

INF = 10000000000000000000000000000

def dijkstra(store,n):
    
    q = []

    distance = [INF]*(n+1)
    
    #모든 편의점 정점들을 우선순위 큐에 넣는다.
    #모든 편의점 정점들이 출발 정점이 되고, 거리는 모두 0이 된다.
    for s in store:
        
        heapq.heappush(q,(0,s))
        distance[s] = 0
    
    #다익스트라 알고리즘을 수행하면서,
    #모든 편의점 정점들에 대하여, 가장 거리가 짧은 경우가 distance에 기록될 것
    while q:
        
        dist,u = heapq.heappop(q)

        if distance[u] < dist:
            
            continue
        
        for b,c in graph[u]:
            
            cost = dist + c

            if distance[b] > cost:
                
                distance[b] = cost
                heapq.heappush(q,(cost,b))
    
    return distance

n,m = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    
    a,b,c = map(int,stdin.readline().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

p,q = map(int,stdin.readline().split())

house = list(map(int,stdin.readline().split()))
store = list(map(int,stdin.readline().split()))

answer = INF+1
min_h = n+1

dist = dijkstra(store,n)

#편의점과 최단거리가 같은 경우, 더 작은 번호의 정점을 출력하기 위해
house.sort()

#집 후보들을 순회해서, 편의점과 최단 거리를 비교
for h in house:
    
    if dist[h] == INF:
        
        continue
    
    if answer > dist[h]:
        
        answer = dist[h]
        min_h = h #house를 정렬해놔서, 이 순간에 기록되는 정점 번호가 결국에 가장 작은 번호의 정점

print(min_h)