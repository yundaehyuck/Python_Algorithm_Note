##최적화된 프림 알고리즘

import heapq

def prim(r,v,adjL): ##임의로 고른 시작 정점, 마지막 정점
    
    MST = [0]*(v+1) ##MST에 포함된 정점 여부 확인

    MST[r] = 1 ##최초 시작점은 MST에 포함


    ##시작 점과 인접한 정점의 정보를 찾는다.
    adj_node = adjL[r]
    heapq.heapify(adj_node) ##우선순위 큐 생성

    s = 0 #최소 신장 트리의 비용

    while adj_node: ##우선 순위 큐가 빌때까지..
        
        w,a = heapq.heappop(adj_node) ##가중치가 가장 작은 간선을 추출

        if MST[a] == 0: ##MST에 포함되지 않았다면..
            
            MST[a] = 1 ##MST에 포함시키고
            s += w ##가중치를 더해준다.

            for edge in adjL[a]: ##MST에 새로 포함된, a와 인접한 정점에 대하여..
                
                if MST[edge[1]] == 0: ##아직 MST에 포함되지 않은 정점이라면..
                    
                    heapq.heappush(adj_node,edge) ##우선순위 큐에 모두 넣어준다
    
    return s


##노드의 수, 간선의 수
v,e = map(int,input().split())

##인접리스트 방식으로 그래프를 표현
adjL = [[] for _ in range(v+1)]

##간선 정보 넣기
for _ in range(e):
    
    a,b,w = map(int,input().split())
    
    ##가중치가 적은 순서대로 정렬해야하므로, 가중치를 먼저 넣자
    adjL[a].append((w,b))
    adjL[b].append((w,a))

prim(0,v,adjL)

"""
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
175
"""