from itertools import combinations

def find_parent(x,parent):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent[x],parent)
    
    return parent[x]

def union(a,b):
    
    a = find_parent(a,parent)
    b = find_parent(b,parent)

    if parent[a] < parent[b]:
        
        parent[a] = parent[b]
    
    else:
        
        parent[b] = parent[a]      

n,m,k = map(int,input().split())

edges = []

for _ in range(m):
    
    u,v,w = map(int,input().split())
    edges.append((w,u,v))

#스패닝 트리는 n-1개의 간선을 가지므로,
#간선 중 n-1개를 선택한 부분집합을 모두 찾는다
combs = combinations(edges,n-1)

answer = 10**18+1

for edge in combs:
    
    cost = 0
    count = 0

    parent = [i for i in range(n+1)]

    for w,u,v in edge:
        
        if find_parent(u,parent) != find_parent(v,parent):
            
            union(u,v)
            cost += (w)
            cost %= k
            count += 1
    
    #순회하는 간선이 n-1개더라도, 반드시 n-1개를 모두 택한다는 보장이 없다
    #부분집합이 스패닝 트리라는 보장이 없기 때문에, n-1개를 선택했는지 반드시 검사해줘야
    if count == n-1:
        
        if answer > cost:
            
            answer = cost

print(answer)