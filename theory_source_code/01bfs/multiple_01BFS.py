from collections import deque

INF = 1000000000000000000000

#multiple zero - one BFS
def bfs(start,graph):
    
    queue = deque()
    
    dist = [INF]*(n+1)
    
    #시작 정점을 모두 큐에 넣고 BFS 수행
    for s in start:
        
        queue.append(s)
        dist[s] = 0
    
    while queue:
        
        x = queue.popleft()
        
        for v in graph[x]:
            
            if dist[v] > dist[x] + 1:
                
                dist[v] = dist[x] + 1
                queue.append(v)
    
    #BFS가 모두 끝나면, 시작 정점들에서 각 정점까지 최단 거리가 구해짐
    return dist

#그래프 구성
n,w = int(input())

graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(w):
    
    a,b = map(int,input().split())
    
    graph[a].append(b)
    graph[b].append(a)

start = list(map(int,input().split()))
target = list(map(int,input().split()))

answer = 0

dist = bfs(start,graph)

#도착 정점까지 거리를 조사해서, 최대거리를 찾는다.
#최대거리가, 바로 모든 도착 정점까지 도달하는데 걸리는 최솟값일것.
#시작 정점에서 동시에 출발하기 때문에
for t in target:
    
    #t까지 도달할 수 있고, 현재 최댓값 answer을 갱신할 수 있다면,
    if dist[t] != INF and answer < dist[t]:
            
        answer = dist[t]

print(answer)