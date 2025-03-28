from sys import stdin

#노드들의 크기 관계가 주어질때, 정확한 순위를 알 수 있는 노드의 수

def dfs(u,g,visited):
    
    for v in g[u]:
        
        if visited[v] == 0:
            
            visited[v] = 1
            dfs(v,g,visited)

n,m = map(int,stdin.readline().split())

g = [[] for _ in range(n+1)] #정방향 간선을 가진 그래프
r_g = [[] for _ in range(n+1)] #역방향 간선을 가진 그래프

for _ in range(m):
    
    a,b = map(int,stdin.readline().split())

    #a < b
    g[a].append(b)
    r_g[b].append(a) 

count = 0

#각 노드 i에 대하여, g에서 dfs, r_g에서 dfs를 수행하여
#각각에서 도달할 수 있는 노드 수 x,y라 하면 x+y = n-1이면
#위로 x명, 아래로 y명 있는데 이게 합이 n-1이라는 것은 현재 i번 노드의 순위를 알 수 있다는 뜻뜻
for i in range(1,n+1):
    
    visited = [0]*(n+1)
    visited[i] = 1

    dfs(i,g,visited)

    x = sum(visited)-1

    visited = [0]*(n+1)
    visited[i] = 1

    dfs(i,r_g,visited)

    y = sum(visited)-1

    if x+y == n-1:
        
        count += 1

print(count)