import heapq
from sys import stdin

def dijkstra(start):

    q = []

    heapq.heappush(q,(0,start))

    distance[start] = 0
    
    #시작 지점과 가장 가까운 노드는 0이라고 초기화
    prev[start] = 0 

    while q:
        
        dist,u = heapq.heappop(q)

        if distance[u] < dist:
            
            continue
        
        for b,c in graph[u]:
            
            cost = dist + c

            if cost < distance[b]:
                
                distance[b] = cost

                heapq.heappush(q,(cost,b))
                
                ## b까지의 최단 거리가 갱신된다면, 
                ## b와 가장 가까운 노드는 u이다.
                prev[b] = u
    

    return prev,distance
        

n = int(stdin.readline())

m = int(stdin.readline())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    
    a,b,c = map(int,stdin.readline().split())

    graph[a].append((b,c))

start,goal = map(int,stdin.readline().split())

INF = 100000000000000

distance = [INF]*(n+1)

##최단 경로를 역추적하기 위한 배열 초기화
prev = [0]*(n+1) 

dir,distance = dijkstra(start)

print(distance[goal])

##실제 최단 경로 역추적하기

s_path = [goal]

##목적지부터 시작
prev_node = goal

while 1:
    
    ##현재 노드와 가장 가까운 이전 노드 prev_node
    prev_node = prev[goal]
    
    ##반복을 통해 이전 노드가 0이라면..
    ##이전 노드가 없다는 말이므로
    ##현재 노드가 출발 노드니까 반복문 탈출
    
    if prev_node == 0: 
        
        break
    
    ##이전 노드가 0이 아니라면..
    else:
        
        ##현재 노드를 최단 경로 리스트에 넣어두고
        s_path.append(prev_node)
        
        ##다음 경로 역추적을 위해 현재 노드를 갱신한다
        goal = prev_node

print(len(s_path))

##추적한 경로를 역순으로 배열하면 실제 최단 경로
print(*s_path[::-1])

"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

4
3
1 3 5
"""