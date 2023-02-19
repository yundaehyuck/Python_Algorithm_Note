from sys import stdin

def find_parent(x,parent):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent[x],parent)
    
    return parent[x]

def union(a,b,parent):
    
    a = find_parent(a,parent)
    b = find_parent(b,parent)

    if parent[a] < parent[b]:
        
        parent[parent[a]] = parent[b]
    
    else:
        
        parent[parent[b]] = parent[a]

v,e = map(int,stdin.readline().split())

graph = [[] for _ in range(v+1)]

parent = [i for i in range(v+1)]

answer = True

for _ in range(e):
    
    a,b = map(int,stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)
    
    if find_parent(a,parent) != find_parent(b,parent):
        
        union(a,b,parent)
    
one = set()

for i in range(1,v+1):
        
    one.add(find_parent(i,parent))
    
if len(one) == 1:
    
    odd = 0

    for row in graph:
        
        if len(row) % 2 == 1:
            
            odd += 1
    
    if odd == 2 or odd == 0:
        
        print("YES")
    
    else:
        
        print("NO")

else:
    
    print("NO")