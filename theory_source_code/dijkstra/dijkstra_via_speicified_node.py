import heapq
from sys import stdin

def dijkstra(start,distance):
    
    q = []

    heapq.heappush(q,(0,start))

    distance[start] = 0

    while q:
        
        dist,u = heapq.heappop(q)

        if distance[u] < dist:
            
            continue
        
        for b,c in graph[u]:
            
            cost = dist + c

            if cost < distance[b]:
                
                distance[b] = cost

                heapq.heappush(q,(cost,b))
    
    return distance

n,e = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    
    a,b,c = map(int,stdin.readline().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

INF = 100000000000000000

v1,v2 = map(int,input().split())

##1,v1,v2를 start로 하는 다익스트라를 3번 적용해서 distance배열 3개를 구함

distance1 = dijkstra(1,[INF]*(n+1))

distance2 = dijkstra(v1,[INF]*(n+1))

distance3 = dijkstra(v2,[INF]*(n+1))

a = distance1[v1]+distance2[v2]+distance3[n] #1>v1>v2>n
b = distance1[v2]+distance3[v1]+distance2[n] #1>v2>v1>n

ans = min(a,b)

if ans >= INF: ##도달할 수 없는 경우는 INF 이상이 되는 경우
    
    print(-1)

else:
    
    print(ans)