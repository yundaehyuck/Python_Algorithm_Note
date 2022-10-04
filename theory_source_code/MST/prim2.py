##변형된 프림 알고리즘

def prim(r,v): ##임의로 고른 시작 정점 r, 마지막 정점 v

    MST = [0]*(v+1)

    MST[r] = 1 ##시작 정점은 이미 MST에 포함

    s = 0 ##최소 비용 신장트리의 가중치 합

    for _ in range(v): ##선택된 r을 뺀 나머지 v개의 정점 선택하기
        
        ##인접한 정점 중에서 최소 비용을 가지는 간선을 연결시키는 정점 선택

        u = 0
        min_w = 10000

        for i in range(v+1):
            
            if MST[i] == 1: ##MST에 포함된 정점 중에서..
                
                for j in range(v+1):
                    
                    ##MST에 포함되지 않았고, i와 인접하면서.. 최소 가중치인 j를 찾는다
                    if adjM[i][j] > 0 and MST[j] == 0 and min_w > adjM[i][j]:
                        
                        u = j
                        min_w = adjM[i][j]
        
        s += min_w
        MST[u] = 1 ##그렇게 선택된 정점 u를 MST에 추가
    

    return s


v,e = map(int,input().split())

adjM = [[0]*(v+1) for _ in range(v+1)]

for _ in range(e):
    
    a,b,w = map(int,input().split())

    adjM[a][b] = w
    adjM[b][a] = w

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