import heapq
from sys import stdin

n,r = map(int,stdin.readline().split())

graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(r):
    
    a,b,c,d,e = map(int,stdin.readline().split())

    if e <= 10:
        
        cost = c
    
    else:
        
        cost = c + (e-10)*d

    graph[a].append((b,cost))

INF = 1000000000000000000000000000

queue = []

distance = [[INF,INF] for _ in range(n+1)]

heapq.heappush(queue,(0,1,1))

distance[1] = [0,0]

while queue:
    
    dist,count,v = heapq.heappop(queue)

    if distance[v][0] < dist:
        
        continue
    
    for u,c in graph[v]:
        
        cost = dist + c

        if distance[u][0] > cost:
            
            distance[u][0] = cost
            distance[u][1] = count+1

            heapq.heappush(queue,(cost,count+1,u))
        
        elif distance[u][0] == cost:
            
            if distance[u][1] > count+1:
                
                distance[u][1] = count+1

                heapq.heappush(queue,(cost,count+1,u))

if distance[n][0] == INF:
    
    print('It is not a great way.')

else:
    
    print(distance[n][0], distance[n][1])