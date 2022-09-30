##path compression
##반복 구조를 이용한 find함수
##원소 x의 대표자를 찾는다

def find_parent(parent,x):
    
    while parent[x] != parent[parent[x]]:
        
        parent[x] = parent[parent[x]]
    
    return parent[x]

"""##재귀로 구현한 find

def find_parent(parent,x):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent,parent[x])
    
    return parent[x]"""


##union by rank

def union_parent(parent,a,b):
    
    #a,b의 대표자를 찾는다
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    ##rank가 낮은 집합의 부모를 rank가 높은 집합의 노드 번호로
    ##부등호를 어떻게 설정하느냐에 따라, 어떤 것이 최종 루트가 될지 달라지니 생각을 잘 해야함
    ##얘는 근데 그냥 안하는게 좋겠는데??
    ##루트를 설정하는게 마음대로 안되는데.. 허허

    if rank[a] > rank[b]:
        
        parent[b] = a
    
    else:
        
        parent[a] = b

  ##rank가 서로 동일하면, rank를 1 증가
        if rank[a] == rank[b]:
            
            rank[b] += 1

v,e = map(int,input().split())

parent = [0]*(v+1)

##node i의 높이를 저장할 rank
##초기 rank는 1로 하는 사람도 있는듯?
rank = [0]*(v+1) ##rank를 저장할 초기화된 리스트 

##초기에 부모 테이블을 자기 자신으로 설정함
for i in range(1,v+1):
    
    parent[i] = i

##union 연산을 수행

for i in range(e):
    
    a,b = map(int,input().split())
    union_parent(parent,a,b)

##각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end = '')
for i in range(1,v+1):
    
    print(find_parent(parent,i),end= ' ')

print()

##부모 테이블 출력

print('부모 테이블: ', end='')

for i in range(1,v+1):
    
    print(parent[i],end=' ')


"""
6 4
1 4
2 3
2 4
5 6
각 원소가 속한 집합: 4 4 4 4 6 6 
부모 테이블: 4 4 4 4 6 6 
"""