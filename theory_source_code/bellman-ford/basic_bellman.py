INF= int(1e9) #무한을 의미하는 값

#벨만 포드 알고리즘
def bf(start):
    
    #시작 노드에 대해 거리를 0으로 초기화

    dist[start] = 0

    #n-1번의 라운드를 반복한다
    #음수 간선의 순환을 탐지하고자 한다면, 1번 더 반복해서 n번을 반복한다

    for i in range(n):
        
        #매 라운드마다 존재하는 모든 간선을 확인한다
        for j in range(m):
            
            u = edges[j][0]
            v = edges[j][1]

            cost = edges[j][2]

            #시작점에서 현재 간선에 도달할 수 있고(dist[u]가 무한이 아니다)
            #도착점의 현재 최단거리가, 시작점을 거쳐서 가는 비용보다 큰 경우에..

            if dist[u] != INF and dist[v] > dist[u] + cost:
                
                #최단 거리를 갱신
                dist[v] = dist[u] + cost

                #n-1번 모두 갱신시키고 나서
                #n번째 라운드에서조차도 값이 갱신된다면.. negative cycle이 존재하는 것이다
                if i == n-1:
                    
                    return True
    
    return False #negative cycle이 존재하지 않음


#노드의 개수, 간선의 개수

n,m = map(int,input().split())

#간선에 대한 정보

edges = []

for _ in range(m):
    
    #노드 a에서 노드 b로 가는 비용이 c이다.
    a,b,c = map(int,input().split())

    edges.append((a,b,c))

#최단 거리 테이블을 모두 무한으로 초기화

dist = [INF] * (n+1)

#벨만 포드 알고리즘을 수행한다

negative_cycle = bf(1) #출발노드는 1이라고 설정

if negative_cycle: #음수 순환이 존재하면..
    
    print(-1)

else: #음수 순환이 존재하지 않는다면..
    
    for i in range(2,n+1): #1번 말고 다른 노드까지 도달 최단 거리
        
        if dist[i] == INF: #최단거리가 갱신되지 않았다면 도달 불가능
            
            print(-1)
        
        else: #최단 거리가 갱신되었다면 도달 가능
            
            print(dist[i])