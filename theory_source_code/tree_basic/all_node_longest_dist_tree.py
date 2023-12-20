#트리에서 모든 정점 각각에서 가장 먼 거리
from sys import stdin,setrecursionlimit
setrecursionlimit(50000)

#u에서 자식까지 가장 먼 거리
def find_depth(u):

    for v,w in tree[u]:

        if visited[v] == 0:

            visited[v] = 1
            find_depth(v) #u에서 자식 v로 계속 내려간 다음,
            #리프 노드부터 w씩 증가시키면서 올라오는데
            #u에서 내려가는 길은 여러가지일 수 있으니, max값으로 갱신
            depth[u] = max(depth[u],depth[v]+w)

def dfs(u):
    
    #u에서 자식까지 가장 먼 거리 d1, 두번째로 먼 거리 d2를 구한다
    d1 = 0
    d2 = 0
    
    #u의 자식 v를 모두 순회하여, v에서 자식까지 가장 먼 거리 depth[v]에
    #v에서 u까지 거리 w의 합 depth[v]+w중 1번째로 큰 값, 2번째로 큰 값을 구한다.
    for v,w in tree[u]:
        
        if visited[v] == 0:

            x = depth[v]+w

            if d1 < x: #x가 d1보다 크면,

                d2 = d1 #이전 d1은 2번째로 큰 값이고
                d1 = x #x는 새로운 가장 큰 값
            
            elif d2 < x: #x가 d1보다 작은데, d2보다 크다는 것은.. x가 2번째로 큰 값
                
                d2 = x
    
    #d1,d2를 구했으면, v에서 위쪽으로 가장 먼 거리 dist[v]를 구한다.
    for v,w in tree[u]:
        
        if visited[v] == 0:
            
            visited[v] = 1

            x = depth[v] + w
            
            #u의 자식 v에 대하여... 
            #가장 먼 거리 d1이 depth[v]+w와 같다는 것은 v가 d1위에 놓여있다
            #이 경우 v에서 위쪽으로 가장 먼 거리는.. dist[v] = max(dist[u],d2)+w
            if d1 == x:
                
                dist[v] = max(dist[u],d2)+w 
            
            #d1이 x와 다르다면, v는 d1위에 있지 않다.
            #v에서 위쪽으로 가장 먼 거리는.. dist[v] = max(dist[u],d1)+w
            else:
                
                dist[v] = max(dist[u],d1)+w
            
            #다음 자식으로 이동
            dfs(v)

n = int(stdin.readline())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):

    u,v,w = map(int,stdin.readline().split())
    tree[u].append((v,w))
    tree[v].append((u,w))

depth = [0]*(n+1)
dist = [0]*(n+1)

#정점 u에서 자식까지 가장 먼 거리 depth를 구한다
visited = [0]*(n+1)
visited[1] = 1
find_depth(1)

#정점 u에서 위쪽으로 가장 먼 거리 dist를 구한다
visited = [0]*(n+1)
visited[1] = 1
dfs(1)

#정점 u에서 가장 먼 거리는, depth와 dist중 더 큰 값이다.
for i in range(1,n+1):
    
    print(max(dist[i],depth[i]))