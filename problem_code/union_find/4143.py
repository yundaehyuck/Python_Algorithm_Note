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

t = int(stdin.readline())

for _ in range(t):
    
    n = int(stdin.readline())

    map_dict = {}

    i = 0
    
    parent = [j for j in range(2*n+1)]

    rank = [1] * (2*n+1)

    for _ in range(n):
        
        a,b = stdin.readline().rstrip().split()

        if map_dict.get(a,-1) == -1:

            map_dict[a] = i

            i += 1
        
        if map_dict.get(b,-1) == -1:

            map_dict[b] = i

            i += 1
            
        union(map_dict[a],map_dict[b],parent)

        print(rank[find_parent(map_dict[a],parent)])