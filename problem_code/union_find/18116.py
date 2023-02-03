from sys import stdin

def find_parent(x,parent):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent[x],parent)
    
    return parent[x]

def union(a,b,parent):
    
    a = find_parent(a,parent)
    b = find_parent(b,parent)

    if a != b:

        if rank[a] > rank[b]:
            
            parent[b] = a
        
        else:
            
            parent[a] = b
        
        rank[a] += rank[b]
        rank[b] = rank[a]

N = int(stdin.readline())

n = 10**6
parent = [0]*(n+1)
rank = [1]*(n+1)

for i in range(1,n+1):
    
    parent[i] = i

for _ in range(N):
    
    c = stdin.readline().rstrip().split()

    if c[0] == 'I':
        
        union(int(c[1]),int(c[2]),parent)
    
    else:
        
        p = find_parent(int(c[1]),parent)
        
        print(rank[p])