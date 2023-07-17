#boj 13290
import heapq
from sys import stdin

n = int(stdin.readline())

items = list(map(int,stdin.readline().split()))

graph = [[]*(n+1) for _ in range(n+1)]

m = int(stdin.readline())

#각 노드가 가지는 아이템의 수도 그래프에 넣어준다
for _ in range(m):
    
    a,b,d = map(int,stdin.readline().split())

    graph[a].append((b,d,items[b-1]))
    graph[b].append((a,d,items[a-1]))

queue = []

INF = 10000000000000000000000

#distance[i]를 i번 노드까지 도달하는데 걸린 [비용,아이템 수 합]
distance = [[INF,0] for _ in range(n+1)]

distance[1] = [0,items[0]] #출발 노드에서 출발노드로 가는 비용은 0, 아이템 수는 items[0]

#큐에는 (1우선순위, 2우선순위, 노드)로 넣어준다 (비용, 아이템 수, 노드)
heapq.heappush(queue,(0,items[0],1))

while queue:
    
    dist,item,v = heapq.heappop(queue)

    if distance[v][0] < dist: #제1우선순위가 더 작다면, 이미 갱신된거니 넘겨주고
        
        continue
    
    for u,c,i in graph[v]:
        
        cost = dist + c
        pick = item + i

        if distance[u][0] > cost: #제1 우선순위 새 비용이 더 작다면, 갱신해주는데
            
            distance[u][0] = cost
            distance[u][1] = pick #제2 우선순위인 아이템 수를 갱신해주는것 잊지말고
            heapq.heappush(queue,(cost,pick,u))
        
        elif distance[u][0] == cost: #제1 우선순위가 동일하다면...
            
            if distance[u][1] < pick: #제2우선순위 아이템수를 최대화시켜줘야한다
                
                distance[u][1] = pick
                heapq.heappush(queue,(cost,pick,u))
    
if distance[n][0] == INF: #거리가 INF라면 도달 불가능한경우
    
    print("impossible")

else:
    
    print(distance[n][0], distance[n][1])