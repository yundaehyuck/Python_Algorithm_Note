from sys import stdin

def find_parent(x,parent):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent[x],parent)
    
    return parent[x]

def union(a,b,parent):
    
    #a,b의 대표자를 찾는다
    a = find_parent(a,parent)

    b = find_parent(b,parent)
    
    #a의 친구비가 b의 친구비보다 많다면...
    if A[a] > A[b]:
        
        #a가 b에 들어가도록
        #a의 부모를 b로 설정
        parent[a] = b
    
    else:
        
        #a의 친구비가 b의 친구비보다 적다면..
        
        #b가 a에 들어가도록
        #b의 부모를 a로 설정
        parent[b] = a

n,m,k = map(int,stdin.readline().split())

A = [0] + list(map(int,stdin.readline().split()))

parent = [0]*(n+1)

for i in range(1,n+1):
    
    parent[i] = i

for _ in range(m):
    
    v,w = map(int,stdin.readline().split())

    union(v,w,parent)

answer = 0

check = [0]*(n+1)

for p in parent[1:]:
    
    #p의 대표자를 찾아서 해당 index가 최종적으로 어디 집합에 속하는지를 찾습니다
    p = find_parent(p,parent)
    
    if check[p] == 0:
        
        answer += A[p]
        check[p] = 1

if answer <= k:
    
    print(answer)

else:
    
    print('Oh no')