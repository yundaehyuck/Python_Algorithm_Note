#그래프를 두 집합으로 분리하기
from sys import stdin

def find_parent(x,parent):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent[x], parent)
    
    return parent[x]

def union(a,b,parent):

    if parent[a] > parent[b]:
        
        parent[a] = b
    
    else:
        
        parent[b] = a

n,m = map(int,stdin.readline().split())

edges = []

answer = 0

for _ in range(m):
    
    a,b,c = map(int,stdin.readline().split())

    edges.append((c,a,b))

#edges.sort()를 하면, (c,a,b)에서 c가 동일하면 a를 기준으로 정렬하므로
#시간이 조금 느려진다
#크루스칼 알고리즘에선, 첫번째 간선 가중치만을 기준으로 정렬하면 되니까.. 

#다음과 같이 하면 조금 시간확보 가능
edges.sort(key=lambda x: x[0])

parent = [i for i in range(n+1)]

count = 0

#n-2개의 간선을 선택한 최소 스패닝 트리를 만들면, 
#각 집합 내 정점이 서로 연결된 두 집합으로 분리된다
for c,a,b in edges:
    
    if count == n-2: #간선이 1개만 있는 그래프때문에 count == n-2를 먼저 써줘야함
        
        break
    
    a = find_parent(a,parent)
    b = find_parent(b,parent)
        
    if a != b:
        
        union(a,b,parent)
        answer += c
        
        count += 1
    
print(answer)