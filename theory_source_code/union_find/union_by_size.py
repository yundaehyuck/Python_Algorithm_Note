##union by size

##rank 배열을 집합의 크기로 저장

def union_parent(parent,a,b):

    
    ##a,b의 대표자를 찾고
    
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    ##a,b가 서로 다르다면 union을 수행
    
    if a != b:
        
    ##크기가 작은 집합의 부모를 크기가 큰 집합으로
        
        if rank[a] > rank[b]:
            
            parent[b] = a
        
        else:
            
            parent[a] = b
        
        ##union 되어서 집합의 크기를 변경
        
        rank[a] += rank[b]
        
        rank[b] = rank[a]
    
    

parent = [i for i in range(v+1)] ##최초 부모는 자기 자신으로 설정

rank = [1]*(v+1) ##각 집합의 크기를 저장