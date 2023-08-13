#Binary Lifting + DP를 이용한 최소 공통 조상 찾기
#2의 거듭제곱꼴로 부모 노드를 거슬러 올라간다

import sys
from sys import stdin
sys.setrecursionlimit(10**5)

#트리 구성
n = int(stdin.readline())

tree = [[] for _ in range(n+1)]

#트리의 노드 수가 N개이면 간선의 수는 N-1개

for _ in range(n-1):
    
    u,v = map(int,stdin.readline().split())

    tree[u].append(v)
    tree[v].append(u)

#dfs를 이용해 루트 노드부터 각 노드의 깊이, 부모 노드 정보를 구한다.

max_two = 21 #2^20 = 약 100만(최대 노드 수가 약 100만개 정도라고 가정)

depth = [0]*(n+1) #노드의 깊이

#노드의 부모
#parent[u][i] = u 노드의 2^i번째 부모 노드
parent = [[0]*(max_two) for _ in range(n+1)] 
visited = [0]*(n+1)

#루트 노드가 1번
visited[1] = 1

#v노드가 깊이 d이고, dfs 수행
def dfs(v,d):
    
    #v에 연결된 u 노드 정보를 파악
    for u in tree[v]:
        
        if visited[u] == 0: #u를 아직 방문하지 않았다면..
            
            visited[u] = 1 #u를 방문처리

            depth[u] = d + 1 #u는 v 한단계 아래니까, 깊이는 v의 깊이 + 1

            parent[u][0] = v #v에서 u로 내려왔으므로, u의 부모는 v

            dfs(u,d + 1) #다음 u로 깊이 d+1을 가지고 dfs수행

#먼저 모든 노드의 한단계 위 부모를 구한다.
dfs(1,0)

#다이나믹 프로그래밍을 이용해 모든 노드의 2의 거듭제곱꼴 부모를 구한다.
def dp_parent(parent):
    
    for i in range(1,max_two): #i = 0은 구해졌고, i = 1 ~ max_two-1까지
        
        for j in range(1,n+1): #j는 노드번호로 1부터 n까지
            
            #j에서 2^i-1올라가고 2^i-1올라간 것은 j에서 2^i만큼 올라간것과 같다.
            #j >> parent[j][i] >> parent[parent[j][i-1]][i-1]로 유도된 부모 관계 점화식
            parent[j][i] = parent[parent[j][i-1]][i-1]

#모든 노드의 2^i번째 부모 노드를 구한다.
dp_parent(parent)

#두 노드 a,b의 최소 공통 조상을 찾는다
def lca(a,b):
    
    #b의 노드 깊이가 더 깊도록 맞춰준다.
    if depth[a] > depth[b]:
        
        a,b = b,a
    
    #max_two - 1에서 0까지 2의 거듭제곱 지수 i를 감소시켜가면서,
    #두 노드의 깊이 차이가 2의 i제곱보다 크거나 같다면, 
    #일단 2의 i제곱만큼 거슬러 올라간다
    for i in range(max_two-1,-1,-1):
        
        if depth[b] - depth[a] >= (2**i):
            
            b = parent[b][i]
    
    #반복문이 끝나면 두 노드의 깊이 차이는 0이 된다.
    #왜냐하면 모든 자연수는 2의 거듭제곱 합으로 표현되기 때문이다.
    
    #두 노드 깊이 차이가 짝수이냐 홀수이냐에 따라..
    #(짝수) 14 >>(i = 3) 6 >> (i = 2) 2 >> (i = 1) 0
    #(홍수) 13 >>(i = 3) 5 >> (i = 2) 1 >> (i = 0) 0
    
    #두 노드가 동일한 깊이가 되었을때, 서로 같은 노드라면 바로 return
    if a == b:
        
        return a
    
    #max_two - 1에서 0까지 2의 거듭제곱 지수 i를 감소시켜가면서,
    #2^i만큼 위 부모 노드가 서로 다르다면 거슬러 올라간다.
    for i in range(max_two-1,-1,-1):
        
        if parent[a][i] != parent[b][i]:
            
            a = parent[a][i]
            b = parent[b][i]
    
    #신기하게도 반복문이 끝나면 바로 1단계 위 부모노드가 최소 공통 조상이 된다.
    
    #최소공통조상까지 차이가 짝수이냐 홀수이냐에 따라..
    #(짝수) 14 >>(i = 3) 6 >> (i = 2) 2 >> (i = 0) 1
    #(홀수) 13 >>(i = 3) 5 >> (i = 2) 1
    return parent[a][0]

#쿼리를 받아, a,b의 최소 공통 조상을 구해준다.
m = int(stdin.readline())

for _ in range(m):
    
    a,b = map(int,stdin.readline().split())

    print(lca(a,b))