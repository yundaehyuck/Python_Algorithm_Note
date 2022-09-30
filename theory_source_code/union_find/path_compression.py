##path compression

##find함수를 호출하고 바로 부모 테이블을 갱신함

def find_parent(parent,x):
    
    if parent[x] != x:
        
        parent[x] = find_parent(parent,parent[x])
    
    return parent[x]


"""기본함수와 비교

def find_parent(parent,x):
    
    if parent[x] != x:
        
        return find_parent(parent,parent[x])
    
    return x
"""

##반복문 구현 path compression(효율이 조금 떨어짐)

def find_parent(parent,x):
    
    while parent[x] != parent[parent[x]]:
        
        parent[x] = parent[parent[x]]
    
    return parent[x]
    
"""기본 함수와의 비교
def find_parent(parent,x):
    
    while x != parent[x]:
        
        x = parent[x]
    
    return x
"""