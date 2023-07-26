## 특정 원소가 속한 집합을 찾는 함수

##path compression 적용

def find_parent(parent,x):
    
    ##루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출

    if x != parent[x]:
        
        parent[x] = find_parent(parent,parent[x])
    
    return parent[x]

"""
def find_parent(parent,x):
    
    while parent[x] != parent[parent[x]]:
        
        parent[x] = parent[parent[x]]
    
    return parent[x]
"""

##두 원소가 속한 집합을 합치는 함수

##union by rank 적용

def union_parent(parent,a,b):
    
    ##a,b의 대표자를 찾고
    #a = find_parent(parent,a)
    #b = find_parent(parent,b) ##edge 선택에서 미리 a,b의 대표자를 찾아온다
    
    ##rank가 낮은 부모를 높은 노드 번호로
    if rank[a] > rank[b]:
        
        parent[b] = a
    
    else:
        
        parent[a] = b

        if rank[a] == rank[b]: ##rank가 동일하면
            
            rank[b] += 1 ##한쪽 rank를 1 증가

"""
def union_parent(parent,a,b):
    
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if parent[a] > parent[b]:
        
        parent[parent[b]] = parent[a]
    
    else:
        
        parent[parent[a]] = parent[b]
"""


##노드와 간선의 개수 입력받는다

v,e = map(int,input().split())

##부모 테이블 초기화

parent = [0]*(v+1)
rank = [0]*(v+1) ##union by rank를 위한 rank배열

##최초 부모를 자기 자신으로 초기화함

#parent = [i for i in range(v+1)]

for i in range(1,v+1):
    
    parent[i] = i


##모든 간선을 담을 리스트와 최종 비용

edges = []

result = 0

##모든 간선에 대한 정보 받기

for _ in range(e):
    
    a,b,cost = map(int,input().split())

    edges.append((cost,a,b)) ##cost가 작은 순으로 오름차순 정렬을 위해 cost를 앞에 두기

##간선을 가중치 비용 순서대로 오름차순 정렬

#edges.sort()

#edges.sort()를 하면, (c,a,b)에서 c가 동일하면 a를 기준으로 정렬하므로
#시간이 조금 느려진다
#크루스칼 알고리즘에선, 첫번째 간선 가중치만을 기준으로 정렬하면 되니까.. 

#다음과 같이 하면 조금 시간확보 가능
edges.sort(key=lambda x: x[0])

##크루스칼 알고리즘

cnt = 0 ##최소신장트리를 위해 선택한 간선의 개수

for edge in edges:
    
    cost,a,b = edge ##비용이 적은 간선을 하나씩 확인하여

    ##노드 a와 노드 b가 동일한 집합에 속하지 않는다면..
    ##즉 사이클이 발생하지 않는다면..
    ##즉 find_parent()값이 서로 다르다면..

    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a != b: ##동일한 집합에 속하지 않는 경우
        
        union_parent(parent,a,b) ##union 수행
        result += cost ##union을 수행한 간선의 가중치를 더해준다

        cnt += 1 ##해당 간선 선택
    
    if cnt == v-1: ##정점의 수 -1만큼의 간선을 선택하면
        
        break ##더 이상 선택할 필요가 없다


print(result) ##최소신장트리의 최소비용