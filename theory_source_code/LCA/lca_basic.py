#최소 공통 조상 기본 해법(O(N))

from sys import stdin
import sys
sys.setrecursionlimit(10**5)

#n개의 노드와 n-1개의 간선을 가진 트리를 인접리스트로 구성
n = int(stdin.readline())

tree = [[] for _ in range(n+1)]

for _ in range(n-1): #참고로 트리의 노드가 n개이면 간선은 n-1개
    
    u,v = map(int,stdin.readline().split())
    
    #트리의 간선은 양방향이기 때문에..
    tree[u].append(v)
    tree[v].append(u)

#루트 노드로부터 각 노드의 깊이와 부모를 계산

depth = [0]*(n+1)   #각 노드의 루트 노드에서부터 깊이
parent = [0]*(n+1)  #각 노드의 부모 노드
visited = [0]*(n+1) #각 노드의 방문 여부

#루트 노드는 1번이고, 깊이는 0으로 초기화
visited[1] = 1

def dfs(v,d):
    
    for u in tree[v]: #v에 연결된 정점 u를 순회하여,
        
        if visited[u] == 0: #u를 아직 방문하지 않았다면..
            
            visited[u] = 1 #u를 방문하고
            
            depth[u] = d + 1  #u의 깊이는 d+1이다.
            
            #트리는 v에서 시작해서 u로 내려가는 구조니까, 
            #u의 부모가 v가 된다.
            
            parent[u] = v 
            
            #그리고 다음 u로 깊이 d+1을 가져가며 dfs 수행
            dfs(u, d + 1)

#루트노드는 1번이고, 깊이는 0으로 dfs 시작
dfs(1,0)

"""
#bfs도 가능한데 재귀가 없어서 시간이 빨라질 수 있다
def bfs(v,d):
    
    queue = deque([(v,d)])
    
    while queue:
        
        v,d = queue.popleft()
        
        for u in tree[v]:
            
            if visited[u] == 0:
                
                depth[u] = d+1
                visited[u] = 1
                parent[u] = v
                queue.append((u,d+1))
 
bfs(1,0)
"""

#u,v의 최소 공통 조상 찾기
def lca(u,v):
    
    #u,v의 깊이가 서로 다르다면, 깊이를 서로 맞춰준다.
    while depth[u] != depth[v]:
        
        #깊이가 더 깊다면, 더 아래에 있다는 뜻이므로,
        if depth[u] > depth[v]:
            
            #u가 더 깊다면, u에서 부모로 한단계 거슬러 올라간다.
            #u의 부모 parent[u]를 u로 갱신
            u = parent[u]
        
        else:
            
            #v가 더 깊다면, v에서 부모로 한단계 거슬러 올라간다.
            #v의 부모 parent[v]를 v로 갱신
            v = parent[v]
    
    #깊이가 서로 맞춰졌다면, u,v의 부모가 서로 같을때까지 거슬러 올라간다.
    while u != v:
        
        #부모가 서로 다르다면, 한단계씩 동시에 거슬러 올라간다.
        #u의 부모 parent[u]를 u로 갱신
        #v의 부모 parent[v]를 v로 갱신
        u = parent[u]
        v = parent[v]
    
    #부모가 서로 동일해졌다면, 그 값이 u,v의 최소 공통 조상
    return u

m = int(stdin.readline())

for _ in range(m):
    
    u,v = map(int,stdin.readline().split())

    print(lca(u,v))