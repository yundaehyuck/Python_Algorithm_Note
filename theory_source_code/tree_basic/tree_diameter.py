#트리의 지름을 찾는 방법
from sys import stdin,setrecursionlimit
setrecursionlimit(100000)

def dfs(u,path):
    
    global diameter,leaf

    if diameter < path:
        
        diameter = path
        leaf = u
        
    visited[u] = 1

    for v,w in tree[u]:
        
        if visited[v] == 0:
            
            dfs(v,path+w)

n = int(stdin.readline())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    
    a,b,w = map(int,stdin.readline().split())

    tree[a].append((b,w))
    tree[b].append((a,w)) #리프에서 리프로 가는 경로를 찾아야해서, 자식 - 부모도 넣어준다

#아무 노드에서나 시작해서, 가장 멀리있는 노드(leaf)를 찾는다
diameter = 0
leaf = -1
visited = [0]*(n+1)
dfs(1,0)

#가장 멀리 있는 노드(leaf)에서 시작해서 가장 길이가 긴 경로를 찾으면 그것이 트리의 지름
visited = [0]*(n+1)
dfs(leaf,0)

print(diameter)