from sys import stdin

def find_parent(x,parent):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent[x],parent)
    
    return parent[x]

def union(a,b):
    
    a = find_parent(a,parent)
    b = find_parent(b,parent)

    if parent[a] < parent[b]:
        
        parent[b] = a
    
    else:
        
        parent[a] = b
    
n,m = map(int,stdin.readline().split())

edges = []

for _ in range(m):
    
    a,b,c = map(int,stdin.readline().split())

    edges.append((c,a,b))

parent = [i for i in range(n+1)]

#최대 비용을 가지는 신장 트리를 만들기 위해
#내림차순으로 정렬
edges.sort(reverse=True)

answer = 0
count = 0

for c,a,b in edges:

    if find_parent(a,parent) != find_parent(b,parent):

        union(a,b)
        count += 1
        answer += c

    if count == n-1:

        break

#n-1개의 간선을 선택하지 못했다면..
#모든 간선을 확인해봐도.. 신장 트리를 구성하지 못했다
if count != n-1:

    print(-1)

else:

    print(answer)