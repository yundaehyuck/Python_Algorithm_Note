from sys import stdin,setrecursionlimit
setrecursionlimit(200000)

def dfs(u):
    
    #양수면 현재 u에서 구매해야하는 흙의 양
    #음수면 현재 u에서 다음 정점으로 가지고 갈 수 있는 흙의 양
    c = B[u] - A[u] 
    
    #자식 정점으로 이동
    for v in tree[u]:
        
        if visited[v] == 0:
            
            visited[v] = 1
            #자식 정점 v에서 구매해야하는 흙의 양을 더해주는데
            #현재 정점에서 산을 깎아 내린 경우, c가 음수이고
            #return된 자식 정점에서 구매해야하는 흙의 양에 충당시켜주게 된다

            #1(c=2) > 2(c=-4) > 3(c=2) > 5(c=3 return) > 3(c=2+3=5) > 2(c=-4+5=1) > 1(c=2+1=3)
            #1(c=2) > 2(c=-4) > 3(c=2) > 6(c=-6 > 0 return) > 3(c=2) > 2(c=-4) > 1(c=2)
            #1(c=2) > 2(c=-4) > 4(c=3 return) > 2(c=1+3) > 1(c=2+1+3=6)
            c += dfs(v) 
    
    #더 이상 다음 정점으로 이동할 수 없는 경우(리프노드에 도달)
    #흙을 보유하고 있는 경우(c < 0) = 모든 흙을 버려야함
    #구매해야하는 흙인 경우 부모 정점으로 부담시켜줘야함
    if c < 0:
        
        c = 0

    return c #부모 정점으로 흙을 보내기

n,p = map(int,stdin.readline().split())

A = [0] + list(map(int,stdin.readline().split()))
B = [0] + list(map(int,stdin.readline().split()))

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    
    u,v = map(int,stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [0]*(n+1)
visited[p] = 1

print(dfs(p))