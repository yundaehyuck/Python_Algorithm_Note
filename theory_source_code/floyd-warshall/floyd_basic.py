#플로이드 워셜 알고리즘

INF = int(1e9) ##무한을 의미하는 매우 큰 값

#노드의 개수와 간선의 개수
n = int(input())
e = int(input())

#2차원 인접행렬을 만들고, 모든 값을 무한으로 초기화함
graph = [[INF]*(n+1) for _ in range(n+1)]

#초기 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
#노드는 1번에서 n번까지

for i in range(1,n+1):
    
    graph[i][i] = 0

#각 간선에 대한 정보를 입력받고 그 값으로 인접행렬을 초기화

for _ in range(e):
    
    #a번에서 b번으로 가는 비용은 w

    a,b,w = map(int,input().split())

    graph[a][b] = w

    #a에서 b로 가는 간선이 하나가 아니라면
    #if graph[a][b] > w:
    #    graph[a][b] = w

##점화식 D[a][b] = min(D[a][b], D[a][k]+D[k][b])에 따라 최소 거리를 갱신
##플로이드 워셜 알고리즘 수행

#선택 노드(k) > a > b순서로..
for k in range(1,n+1): ##1번부터 n번까지 노드 선택
    
    for a in range(1,n+1):
        
        for b in range(1,n+1):
            
            #min으로 하면 매우 느리다.
            #graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
            #if 비교문으로 빠르게 할 수 있다
            if graph[a][b] > graph[a][k] + graph[k][b]:

                graph[a][b] = graph[a][k] + graph[k][b]

##수행된 결과 출력

for a in range(1,n+1):
    
    for b in range(1,n+1):
        
        ##도달할 수 없는 경우는 무한을 출력
        ##거리가 최초 INF라면, 도달할 수 없는 경우

        if graph[a][b] == INF:
            
            print("infinity", end =" ")
        
        else: ##도달 가능한 경우 최단 거리 출력
            
            print(graph[a][b], end = " ")
    
    print()

"""
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0
"""