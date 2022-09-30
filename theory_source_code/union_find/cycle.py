#반복구조로 구현한 find 함수
# 원소 x의 대표자를 찾는다

def find_parent(parent,x):
    
    while x != parent[x]:
        
        x = parent[x]
    
    return x

## union 함수
## 두 원소 a,b를 하나로 합친다

def union_parent(parent,a,b):
    
    a = find_parent(parent,a) #a의 대표자를 찾고
    b = find_parent(parent,b) #b의 대표자를 찾고

    if a < b: #더 큰 번호의 부모를 더 작은 번호로 설정
        
        parent[b] = a
    
    else:
        
        parent[a] = b

#노드의 개수와 간선의 개수

v,e = map(int,input().split())
parent = [0]*(v+1) #부모 번호를 저장할 리스트

##처음엔 자기 자신을 부모로 가지도록 초기화

for i in range(1,v+1):
    
    parent[i] = i

cycle = False ##현재 그래프에서 cycle 발생 여부


#그래프의 모든 간선을 확인
for i in range(e):
    
    a,b = map(int,input().split()) ##간선을 받고
    
    ##루트 노드가 서로 동일하다면.. 사이클 발생
    if find_parent(parent,a) == find_parent(parent,b):
        
        cycle = True
        break 
    
    else: ##루트 노드가 다르다면..
        
        union_parent(parent,a,b) ##(a,b)의 union 수행

if cycle:
    
    print('사이클이 발생했습니다.')

else:
    
    print('사이클이 발생하지 않았습니다.')

"""
3 3
1 2
1 3
2 3
사이클이 발생했습니다.
"""