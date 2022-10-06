import heapq
 
def dijkstra(x,y,n):
     
    q = []
 
    heapq.heappush(q,(0,(x,y)))
 
    distance[y][x] = 0
 
    while q:
         
        dist,(x,y) = heapq.heappop(q)
 
        if distance[y][x] < dist: ##최단거리 배열이, 큐의 최소거리보다 작다면 이미 처리된 노드
             
            continue
         
        ##인접한 곳을 찾아 비용을 계산
 
        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
             
            dx = x + ni
            dy = y + nj
 
            if dx >= 0 and dx <= n-1 and dy >= 0 and dy <= n-1:
                 
                cost = dist + maps[dy][dx]
 
                if cost < distance[dy][dx]: ##원래 비용보다 작으면..
                     
                    distance[dy][dx] = cost ##최소비용으로 갱신하고
 
                    heapq.heappush(q,(cost,(dx,dy))) #큐에 넣고
 
 
T = int(input())
 
for tc in range(1,T+1):
     
    INF = 10000000000
 
    n = int(input())
 
    maps = [list(map(int,input())) for _ in range(n)]
 
    distance = [[INF]*n for _ in range(n)]
 
    print('#'+str(tc),dijkstra(0,0,n))