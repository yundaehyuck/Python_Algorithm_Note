def prim(r,v):  ##임의로 고른 시작 정점 r, 마지막 정점 v
    

    MST = [0]*(v+1) ##정점의 MST 포함 여부
    
    ##key[v]는 MST에 속한 정점과 v가 연결될 때 최소 가중치
    ##최초 key는 가능한 가중치 최댓값 이상으로 초기화해놓는다

    key = [10000]*(v+1)
    
    ##최초 임의로 고른 시작 정점의 key는 0
    key[r] = 0

    for _ in range(v): ##v+1개의 정점 중에서 시작 정점 r을 제외한 v개를 선택한다
        
        ##MST에 포함되지 않은 정점 (MST[u] == 0)중에서 가중치 key가 최소인 u를 찾는 작업

        u = 0
        min_w = 10000

        for i in range(v+1):

            ##MST에 포함되지 않고, 최소의 가중치를 가지는 node를 찾는다.
            if MST[i] == 0 and key[i] < min_w:
                
                u = i
                min_w = key[i]
        
        MST[u] = 1 ##최솟값을 가지는 가중치를 가진 정점 u를 MST에 포함

        ##최초 여기까지는 u = 0일거임.. 나머지는 전부 key 가중치가 10000으로 최대니까

        ##MST에 포함된 u에 인접한 w에 대하여.. MST에 포함되지 않은 정점을 찾는 과정

        for w in range(v+1):
            
            ##인접행렬 값이 0보다 크면 인접해있다는 의미

            if MST[w] == 0 and adjM[u][w] > 0: ##w가 MST에 포함되지 않았고, w가 u에 인접해있으면..
                

                key[w] = min(key[w], adjM[u][w]) ##w의 key와 u-w사이 가중치중 최솟값으로 key[w]를 갱신
        

        ##최초에 u=0이고, u=0과 인접한 모든 w에 대해 최소 비용을 가지는 key[w]를 찾게 될거
        ##다음 반복으로 가면 u = w가 될거고.. 계속 반복..
    

    return sum(key) ##최소 가중치들의 합이 최소 신장 트리의 비용

##노드의 개수와 간선의 개수
v,e = map(int,input().split())

#인접행렬
adjM = [[0]*(v+1) for _ in range(v+1)]

for _ in range(e):
    
    a,b,w = map(int,input().split())

    adjM[a][b] = w
    adjM[b][a] = w ##최소 신장 트리는 무방향 그래프를 가정


prim(0,v)
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