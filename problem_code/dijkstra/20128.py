#짝수 비용 최단 경로, 홀수 비용 최단 경로 찾기
#2의 배수가 되는 최단 경로를 찾는 문제
#k의 배수가 되는 최단 경로를 찾는 알고리즘에서 k = 2
import heapq
from sys import stdin

n,m = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    
    u,v,w = map(int,stdin.readline().split())

    graph[u].append((v,w))
    graph[v].append((u,w))

queue = []

INF = 100000000000000000000000000000000000000

distance = [[INF,INF] for _ in range(n+1)]

distance[1][0] = 0

heapq.heappush(queue,(0,1))

while queue:
    
    dist,v = heapq.heappop(queue)

    if distance[v][dist % 2] < dist:
        
        continue
    
    for u,w in graph[v]:
        
        cost = dist + w
            
        if distance[u][cost % 2] > cost:

            distance[u][cost % 2] = cost
            heapq.heappush(queue,(cost,u))


for i in range(1,n+1):
    
    if distance[i][0] == INF and distance[i][1] == INF:
        
        print(-1,-1)
    
    elif distance[i][0] == INF and distance[i][1] != INF:
        
        print(distance[i][1],-1)
    
    elif distance[i][0] != INF and distance[i][1] == INF:
        
        print(-1,distance[i][0])
    
    else:
        
        print(distance[i][1],distance[i][0])