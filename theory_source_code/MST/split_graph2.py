#그래프 정점들을 두 집합으로 분리하기

from sys import stdin

def find_parent(x,parent):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent[x], parent)
    
    return parent[x]

def union(a,b):
    
    a = find_parent(a,parent)
    b = find_parent(b,parent)

    if parent[a] > parent[b]:
        
        parent[parent[b]] = parent[a]
    
    else:
        
        parent[parent[a]] = parent[b]

n,m = map(int,stdin.readline().split())

edges = []

answer = 0

for _ in range(m):
    
    a,b,c = map(int,stdin.readline().split())

    edges.append((c,a,b))

edges.sort()

parent = [i for i in range(n+1)]

#초기에는 그룹의 수가 정점의 수인 n개만큼 있다
g = n

for c,a,b in edges:
    
    if find_parent(a,parent) != find_parent(b,parent):
        
        union(a,b) # 두 정점을 union 시키면... 하나의 그룹이 되므로..
        answer += c
        
        g -= 1 #그룹의 수가 1개씩 줄어든다..

    if g == 1: #매번 간선을 고르다가, 그룹이 1개가 된다면...
        
        answer -= c #마지막으로 선택된 간선을 제거하고 break
        break
    
print(answer) #그러면 전체 그룹의 수는 2개가 되고, 이때 선택된 간선 가중치 합이 정답