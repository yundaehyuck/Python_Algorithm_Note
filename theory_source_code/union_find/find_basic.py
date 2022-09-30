##특정한 원소 x가 속한 집합을 찾는다
##x가 속한 집합의 대표자를 찾는 함수
##재귀적 구현

def find_parent(parent,x):
    
    ##루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출

    if parent[x] != x:
        
        return find_parent(parent,parent[x])
    
    return x

##반복문 구현

def find_parent(parent,x):
    
    ##루트노드가 아니라면, 루트 노드를 찾을 때까지 반복적으로 거슬러 올라감
    while x != parent[x]:
        
        x = parent[x]
    
    return x