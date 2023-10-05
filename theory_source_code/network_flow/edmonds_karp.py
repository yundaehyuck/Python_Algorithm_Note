from collections import deque
from sys import stdin

INF = 1000000000000000000000000

#경로 path의 유량을 찾는 함수
#경로 path에서 흐를 수 있는 유량은 각 경로를 구성하는 간선이 가지는 잔여 용량들 중 최솟값
def make_flow(s,t,path):
    
    c = INF #잔여 용량의 최솟값

    #끝점 t부터 시작해서 역으로 돌아가면서
    #경로 path의 흐를 수 있는 최소 용량을 찾는다
    #즉, 경로 path를 구성하는 간선들의 잔여 용량중 최솟값을 찾는다.
    v = t

    while v != s: #경로를 역으로 돌면서 시작점 s에 도달했다면 반복문 탈출
        
        #v의 이전 정점 path[v]에서 v로 가는 경로의 잔여 용량이 c보다 작다면,
        #c를 해당 값으로 갱신
        if (capacity[path[v]][v] - flow[path[v]][v]) < c:
            
            c = capacity[path[v]][v] - flow[path[v]][v]

        v = path[v] #v의 이전 정점이 path[v]
    
    #해당 경로에서 흐르는 유량을 찾았으면, 경로를 역추적
    #해당 경로를 구성하는 간선들에 유량을 더해주자
    v = t

    while v != s:
        
        #이전 정점 path[v]에서 v로 가는 유량에 c를 더해주고..
        flow[path[v]][v] += c 

        #유량 대칭성
        #path[v]에서 v로 들어가는 유량과 v에서 path[v]로 나가는 유량이 같다
        flow[v][path[v]] -= c
        v = path[v]
    
    return c

#s에서 t로 가는 '유량이 증가하는 경로'를 찾는 bfs
def bfs(s,t):
    
    queue = deque([s])

    path = [0]*(n+1)

    while queue:
        
        u = queue.popleft()

        for v in graph[u]:
            
            #u에서 v로 용량이 남아(residual) 갈 수 있고 아직 방문하지 않았다면...
            if capacity[u][v] - flow[u][v] > 0 and path[v] == 0:

                queue.append(v)
                path[v] = u #v의 이전 정점이 path[v]

                if v == t: #도착점 sink에 도달했다면....

                    return make_flow(s,t,path) #유량 그래프에 현재 경로에서 흐르는 유량을 기록

    return 0 #더 이상 경로를 찾지 못한 경우

def edmonds_karp(s,t):
    
    path = 0
    
    #s에서 t로 가는 유량이 존재하는지 찾을 수 없을때까지 BFS로 찾는다
    while 1:
        
        c = bfs(s,t)

        if c > 0: #s에서 t로 가는 유량이 존재한다 = 경로가 존재한다 
            
            path += 1
        
        else: #더 이상 흐를 수 있는 유량이 없다 = 경로가 존재하지 않는다
            
            break
    
    return path

n,p = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)] #유량 네트워크

#a > b로 가는 간선이 존재하지 않으면, 용량은 0으로 정의하기 때문에 초기값을 0으로
capacity = [[0]*(n+1) for _ in range(n+1)] #각 간선의 용량

flow = [[0]*(n+1) for _ in range(n+1)] #각 간선에서 흐르는 유량

for _ in range(p):
    
    a,b = map(int,stdin.readline().split())
    
    graph[a].append(b)
    graph[b].append(a) #반대 방향으로 흐르는 유량을 생각해야하므로,
    capacity[a][b] = 1 #a > b로 가는 간선이 존재하는 경우 용량은 1로 제한

source = 1 #유량의 시작점
sink = 2 #유량의 도착점

print(edmonds_karp(source,sink))