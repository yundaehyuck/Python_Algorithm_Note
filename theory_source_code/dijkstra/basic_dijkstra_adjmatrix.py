##다익스트라 알고리즘(인접행렬 표현가능)

def dijkstra(start):
    
    ##시작 노드에 대해 초기화

    distance[start] = 0 ##시작노드 거리는 0

    visited[start] = 1 ##시작 노드 방문 체크

    ##시작 노드에서 다른 노드 i까지 가는 최소 거리는...
    ##인접한 노드까지 거리 그대로

    for i in range(1,v+1):
        
        if adjM[start][i] > 0 and adjM[start][i] < INF: ##i가 start와 인접해있다면..
        
            distance[i] = adjM[start][i]
    
    ##시작 노드를 제외한 전체 v-1개의 노드에 대해 반복

    for _ in range(v-1):
        
        ##현재 distance 배열을 순회하여
        ##최단 거리가 가장 짧은 노드를 선택하여 방문 처리

        u = 0
        min_w = INF

        for i in range(1,v+1): ##정점의 번호가 1번부터 v번까지 일때,
            
            ##아직 방문하지 않았고, 최단거리 distance[i]가 가장 짧은 i를 찾는다
            if visited[i] == 0 and distance[i] < min_w: 
                
                u = i
                min_w = distance[i]
        
        ##반복문을 모두 돌면 최단거리를 가진 노드 u를 찾았다

        visited[u] = 1

        for i in range(1,v+1): ##정점의 번호가 1번부터 v번까지 일때,
            
            if adjM[u][i] > 0 and adjM[u][i] < INF: #u와 인접한 i에 대하여..
                
                #i번 노드의 최단거리는..
                ##현재 최단거리 vs. 선택된 노드 u+u에서 i까지 가는 가중치 중 최솟값으로 갱신
                distance[i] = min(distance[i], distance[u]+adjM[u][i])

##노드의 개수, 간선의 개수를 입력받는다

v,e = map(int,input().split())

##시작 노드 번호를 입력받는다

start = int(input())

##인접행렬 생성
##1번부터 v번까지

adjM = [[0]*(v+1) for _ in range(v+1)]

##방문한 적이 있는지 체크하는 배열

visited = [0]*(v+1)

##최단 거리 테이블을 최초 무한으로 초기화

INF = int(1e9)
distance = [INF]*(v+1)

##모든 간선 정보를 입력받는다

for _ in range(e):
    
    a,b,w = map(int,input().split()) ##a번 노드에서 b번 노드로 가는 가중치가 w

    adjM[a][b] = w ##방향그래프니까 여기까지

##다익스트라 알고리즘 수행
dijkstra(start)

##출발노드에서 1번부터 v번까지 최단거리 출력
for i in range(1,v+1):
    
    if distance[i] == INF: ##최단거리가 무한이면, 갱신되지 않았으므로 도달 불가능
        
        print('infinity')
    
    else: ##최단거리가 무한이 아니면 도달 가능
        
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