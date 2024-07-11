#트리에서 임의의 노드에서 모든 노드를 적어도 1번 이상 방문하는 최소 거리
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

#임의의 노드에서 모든 노드를 1번 이상 방문하고 다시 돌아오는 거리는, 모든 변을 2번 지나면 된다.
#임의의 노드에서 모든 노드를 1번 이상 방문하고 마지막으로 방문하는 정점까지 거리 + 마지막으로 방문한 정점에서 출발점으로 돌아오는 거리
#마지막으로 방문한 정점에서 출발점으로 돌아오는 거리를 최대로 하면, 
#임의의 노드에서 모든 노드를 1번 이상 방문하고 마지막으로 방문하는 정점까지 거리를 최소로 할 수 있다
#마지막으로 방문한 정점에서 출발점으로 돌아오는 거리의 최댓값은 트리의 지름이다
def dfs(u,path):
    
    global diameter, leaf

    if diameter < path:
        
        diameter = path
        leaf = u
    
    visited[u] = 1

    for v,w in tree[u]:
        
        if visited[v] == 0:
            
            dfs(v,path+w)

v = int(input())

tree = [[] for _ in range(v+1)]

total = 0

for _ in range(v-1):
    
    a,b,c = list(map(int,input().split()))
    total += c

    tree[a].append((b,c))
    tree[b].append((a,c))

diameter = 0

#트리의 지름은 어떤 정점에서 dfs로 가장 먼 정점을 찾고
visited = [0]*(v+1)
leaf = -1
dfs(1,0)

#가장 먼 정점에서 가장 먼 정점으로 가는 거리를 구하면 그것이 트리의 지름
visited = [0]*(v+1)
dfs(leaf,0)

print(2*total - diameter)