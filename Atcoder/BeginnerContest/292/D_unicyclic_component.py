def find_parent(x,parent):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent[x],parent)
    
    return parent[x]
 
def union(a,b,parent):
    
    a = find_parent(a,parent)
    b = find_parent(b,parent)
 
    if a == b:
        
        rank[a] += 1
        rank[b] = rank[a]
        return
 
    if rank[a] > rank[b]:
        
        parent[b] = a
    
    else:
        
        parent[a] = b
    
    rank[a] += rank[b]
    rank[a] += 1
    rank[b] = rank[a]
 
n,m = map(int,input().split())
 
parent = [i for i in range(n+1)]
rank = [0]*(n+1)
 
for _ in range(m):
    
    u,v = map(int,input().split())
 
    union(u,v,parent)
 
component = [[] for _ in range(n+1)]
 
for i in range(1,n+1):
    
    s = find_parent(i,parent)
 
    component[s].append(i)
 
yes = True
 
for i in range(1,n+1):
    
    a = len(component[i])
    
    if a != 0:
        
        if rank[i] != len(component[i]):
 
            yes = False
            break
 
if yes:
 
    print("Yes")
 
else:
 
    print("No")