#비감소수열을 이루도록 1번부터 n번까지 가는 최장경로의 길이
from sys import stdin

#union find
def find_parent(x,parent):
    
    if x != parent[x]:
        
        parent[x] = find_parent(parent[x],parent)
    
    return parent[x]

def union(a,b,parent):
    
    a = find_parent(a,parent)
    b = find_parent(b,parent)

    if parent[a] < parent[b]:
        
        parent[a] = b
    
    else:
        
        parent[b] = a

n,m = map(int,stdin.readline().split())

A = [0] + list(map(int,stdin.readline().split()))

graph = [[] for _ in range(n+1)]

parent = [i for i in range(n+1)]

for _ in range(m):
    
    u,v = map(int,stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

    #정점에 적힌 숫자가 서로 같다면, u와 v를 하나의 정점으로 합쳐준다
    if A[u] == A[v]:
        
        union(u,v,parent)

#이제 방향 비순환 그래프에서 정점 v까지 도달하는데 걸리는 최장 경로의 길이를 구하는 문제로 바뀌었다
        
#숫자가 증가하는 순서대로 이동해야하므로, 정점에 적힌 숫자 A배열을 오름차순으로 정렬한다면..
#해당 정점 번호들이 위상정렬된 노드들이 된다.
B = []

for i in range(1,n+1):
    
    B.append((i,A[i]))

B.sort(key = lambda item: item[1])

INF = 10**18

#dp의 초기값을 음의 무한대로 해준다.
#위상정렬된 시작 노드가 1번이 아닐 수 있기 때문
#1번부터 N번까지 이동하는 최장 경로의 길이를 구해야하니까 dp[1] = 1이어야하는데,
#0으로 초기화하면 dp[1] = 1에서 바뀔 수 있어서, 
#즉, 1번 노드 이전의 노드들은 경로의 길이에 영향을 주면 안된다.
dp = [-INF]*(n+1)

#모든 노드는 union find로 합쳐진 상태로 관리되고 있으므로 항상 find_parent()로 대표자로 dp배열에 기록
#parent[1]이랑 find_parent(1,parent)는 다르다.
#find_parent(1,parent) = parent[...parent[parent[parent[1]]]]
dp[find_parent(1,parent)] = 1

for u,_ in B: #위상정렬
    
    u1 = find_parent(u,parent)

    for v in graph[u]:    

        if A[v] > A[u]: #A[u] == A[v]일수 있기 때문에 조건문 사용
            
            v = find_parent(v,parent)
            dp[v] = max(dp[v],dp[u1]+1) #u에서 v로 이동할 수 있을때, dp[v] = max(dp[v],dp[u]+1)이다.

#1번부터 n번까지 이동하는 최장경로의 길이이므로, dp[n]이 답이다.
print(max(0,dp[find_parent(n,parent)]))