from sys import stdin

def find_parent(parent,x):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a != b:

        if rank[a] > rank[b]:
            
            parent[b] = a
        
        else:
            
            parent[a] = b

        rank[a] += rank[b]
        rank[b] = rank[a]

    return rank[find_parent(parent,a)]
        

    
T = int(stdin.readline())

for _ in range(1,T+1):
    
    f = int(stdin.readline())

    parent = [i for i in range(2*f+1)]
    rank = [1]*(2*f+1)

    ind_dict = {}

    ind = 1

    for _ in range(f):
        
        a,b = stdin.readline().rstrip().split()

        if ind_dict.get(a,0) == 0:
            
            ind_dict[a] = ind
            ind += 1
        
        else:
            
            pass
        
        if ind_dict.get(b,0) == 0:
            
            ind_dict[b] = ind
            ind += 1
        
        else:
            
            pass
        
        print(union_parent(parent,ind_dict[a],ind_dict[b]))