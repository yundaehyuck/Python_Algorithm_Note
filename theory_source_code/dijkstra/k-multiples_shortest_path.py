#비용이 k의 배수가 되는 최단 경로를 찾는 문제
import heapq
from sys import stdin

n,m,k = map(int,stdin.readline().split())

s,t = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    
    u,v,w = map(int,stdin.readline().split())

    graph[u].append((v,w))

queue = []

INF = 10000000000000000000000000000000

#distance[i][j] = s에서 i로 가는데 드는 비용 합을 k로 나눈 나머지가 j가 되는 비용의 합의 최솟값
distance = [[INF for _ in range(k)] for _ in range(n+1)]

distance[s][0] = 0

heapq.heappush(queue,(0,s))

while queue:
    
    dist,v = heapq.heappop(queue)

    if distance[v][dist % k] < dist:

        continue

    for u,w in graph[v]:
        
        cost = dist + w
        
        #s에서 u로 가는데 드는 비용의 합 cost를 k로 나눈 나머지에 따라, 최단 비용을 갱신 
        if distance[u][cost % k] > cost:
            
            distance[u][cost % k] = cost
            heapq.heappush(queue,(cost,u))

if distance[t][0] == INF:
    
    print('IMPOSSIBLE')

else:
    
    print(distance[t][0])