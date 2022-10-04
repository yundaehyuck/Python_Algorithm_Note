##다익스트라 알고리즘(인접리스트 표현)

def dijkstra(start):
    
    ##시작 노드에 대해 거리는 0으로 초기화
    distance[start] = 0

    ##시작 노드 방문 처리
    visited[start] = 1

    for b,w in graph[start]: ##시작 정점과 인접한 b와 가중치 w에 대하여
        
        distance[b] = w ##시작 정점에서 b로 가는 최단 거리는 모두 w
    

    ##시작 노드를 제외한 전체 v-1개의 노드에 대해 반복하기

    for _ in range(v-1):
        
        ##distance 배열을 순차탐색하여 
        ##방문하지 않은 노드 중에 최단 거리가 짧은 노드 번호를 찾는다
        
        u = 0
        min_w = INF

        for i in range(1,v+1): ##정점의 번호가 1번부터 v번까지 일때...
            
            if visited[i] == 0 and distance[i] < min_w: ##아직 방문하지 않았고, 거리가 현재 최솟값보다 작을때,
                
                u = i
                min_w = distance[i]
        
        ##반복문을 돌면..최단거리를 가지는 노드 u를 찾았다

        visited[u] = 1

        for b,w in graph[u]: ##u와 연결된 노드 b를 확인한다
            
            ##b까지 가는 최단 비용은..
            ##원래 최단 비용과 (u까지 가는 최단비용+ u에서 b로 가는 가중치w) 사이 최솟값
            distance[b] = min(distance[b], distance[u]+w)


##노드의 개수, 간선의 개수를 입력받는다

v,e = map(int,input().split())

## 시작 노드 번호

start = int(input())

##인접리스트로 노드의 연결 정보

graph = [[] for _ in range(v+1)]

##방문한 적이 있는 노드인지 체크

visited = [0]*(v+1)

##최초 최단 거리 테이블을 무한으로 초기화

INF = int(1e9)

distance = [INF]*(v+1)

##모든 간선 정보를 입력받는다

for _ in range(e):
    
    a,b,w = map(int,input().split())

    ##a번에서 b번으로 가는 비용이 w

    graph[a].append((b,w))


##다익스트라 알고리즘 수행

dijkstra(start)

##각 노드 1번부터 v번까지 가는 최단 비용 출력

for i in range(1,v+1):
    
    if distance[i] == INF: ##무한이면.. 갱신이 안된것으로 도달할 수 없다는 의미
        
        print('infinity')
    
    else: ##도달 가능
        
        print(distance[i])
"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
0
2
3
1
2
4
"""