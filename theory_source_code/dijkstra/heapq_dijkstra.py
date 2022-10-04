#우선순위 큐를 이용한 다익스트라 알고리즘

import heapq

def dijkstra(start):
    
    ##우선순위 큐

    q = []

    ##시작 노드로 가기 위한 최단 거리는 0이며 우선순위 큐에 삽입
    heapq.heappush(q,(0,start))

    distance[start] = 0 ##출발 노드 거리는 0으로 초기화

    ##우선순위 큐가 빌때까지 반복을 수행함

    while q:##큐가 비어있지 않다면..
        
        ##가장 최단 거리가 짧은 노드에 대한 정보를 꺼낸다.

        dist,u = heapq.heappop(q)

        ##현재 노드가 이미 처리된 적이 있다면 무시함

        ##최단거리 테이블의 최단거리가 우선순위 큐의 거리보다 작다면..
        ##이미 처리된 노드이다.
        if distance[u] < dist:
            
            continue
        

        ##선택된 노드와 연결된 인접 노드들을 확인함

        for b,w in graph[u]:
            
            ##연결된 노드들의 최단 비용은...
            ##원래 최단비용 vs. (선택된 노드 u까지 최단비용 dist + u에서 인접한 b까지 가는 최단거리 w) 중 최솟값
            
            ##distance[b] = min(distance[b],dist+w)
            ##최단 거리가 갱신이 되면 우선순위 큐에 넣어야하므로, 다음과 같이 구현함

            cost =  dist + w

            if cost < distance[b]: ##원래 최단비용 distance[b]보다 새로 구한 최단비용 cost가 더 작다면..
                
                distance[b] = cost ##최단거리 테이블을 갱신하고
                heapq.heappush(q,(cost,b)) ##새로 구한 정보를 우선순위 큐에 넣는다


##노드의 개수, 간선의 개수를 입력받는다

v,e = map(int,input().split())

##시작 노드의 번호

start = int(input())

##각 노드에 연결되어 있는 노드에 대한 정보를 담는 인접리스트

graph = [[] for _ in range(v+1)]

##최초 최단 거리 테이블을 무한으로 초기화

INF = int(1e9)
distance = [INF]*(v+1)


##모든 간선의 정보를 입력받는다.

for _ in range(e):
    
    a,b,w = map(int,input().split())

    #a에서 b로 가는 가중치가 w

    graph[a].append((b,w))


##다익스트라 알고리즘 수행

dijkstra(start)

##출발 노드에서 1번부터 v까지 가는 최단경로 출력

for i in range(1,v+1):
    
    ##최단거리 테이블 값이 무한이라면, 도달할 수 없어서 갱신되지 않은 것이다.

    if distance[i] == INF:
        
        print('infinity')
    
    else: ##도달 가능한 경우
        
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