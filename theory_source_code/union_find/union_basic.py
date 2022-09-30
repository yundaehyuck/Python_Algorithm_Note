##두 원소가 속한 집합을 합치는 union 함수

def union_parent(parent,a,b):
    
    a = find_parent(parent,a) ##a의 대표자를 찾고
    b = find_parent(parent,b) ##b의 대표자를 찾고

    if a < b: ##b의 루트노드가 더 크다면,
        
        parent[b] = a ## 더 큰 노드 b의 부모를 더 작은 노드인 a로 설정

    else:  ##a의 루트 노드가 더 크다면
        
        parent[a] = b ## 더 큰 노드 a의 부모를 더 작은 노드인 b로 설정