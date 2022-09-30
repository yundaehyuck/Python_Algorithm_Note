##rank 배열을 쓰지 않고 union by rank

def union(parent,a,b):
    
    ##a,b의 대표자를 찾고
    
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if parent[a] < parent[b]:
       
        parent[parent[a]] = parent[b] ##부모가 작은 값의 부모의 부모를 부모가 큰 값으로?
    
    else:
        
        parent[parent[b]] = parent[a]