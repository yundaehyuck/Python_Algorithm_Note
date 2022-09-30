## union by rank

def union(parent,a,b):
    
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    #if a == b: #루트 노드가 동일하면, 동일한 집합.. 이건 안해도 될듯?
    #    return

    if rank[a] > rank[b]: ##rank가 낮은 집합을 rank가 높은 집합 밑에 붙입니다.
        
        ##rank가 낮은 집합 b의 부모를 rank가 높은 집합 a의 노드 번호로 
        parent[b] = a
    
    else:  ##rank[a] <= rank[b]
        
        ##rank가 낮은 a의 부모를 rank가 높은 b로
        parent[a] = b

        if rank[a] == rank[b]: ##특히 rank가 서로 동일하다면
            rank[b] += 1 ##rank를 1 증가시킵니다.