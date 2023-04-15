import heapq
from sys import stdin

INF = 100000000000000000000000000

def dijkstra(start):

    distance = [INF]*(n)

    q = []

    heapq.heappush(q,(0,start))
    
    distance[start] = 0

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

n,m,x,y = map(int,stdin.readline().split())

graph = [[] for _ in range(n)]

for _ in range(m):

    a,b,c = map(int,stdin.readline().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

dist = dijkstra(y)

dist.sort()

arrive = True

sum_dist = 0

answer = 1

for d in dist[1:]:

    if sum_dist+2*d <= x:
        
        sum_dist += 2*d
    
    else:
        
        if 2*d > x:
            
            arrive = False
            break

        sum_dist = 2*d
        answer += 1


if arrive == False:
    
    print(-1)

else:
    
    print(answer)