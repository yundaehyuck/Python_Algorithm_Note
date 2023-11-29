#정점 U를 루트로 하는 서브트리에서 포함하는 정점의 수
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

def make_tree(current,parent): #현재 노드, 해당 노드의 부모 노드
    
    for node in edges[current]: #현재 노드와 연결된 노드들을 순회하여..
        
        if node != parent: #연결된 노드가 현재 노드의 부모가 아니라면...
            
            tree[current].append(node) #그 노드는 현재 노드의 자식 노드이다.
            make_tree(node,current)

def treedp(current):
    
    for child in tree[current]: #현재 정점의 자식을 순회하여,
        
        treedp(child)
        dp[current] += dp[child] #자식이 가지고 있는 정점의 수를 모두 더해준다     

n,r,q = map(int,stdin.readline().split())

tree = [[] for _ in range(n+1)]
edges = [[] for _ in range(n+1)]

dp = [1]*(n+1) #모든 정점 U를 루트로 하는 서브트리는 U를 일단 1개 포함하고 있다

for _ in range(n-1):
    
    u,v = map(int,stdin.readline().split())

    edges[u].append(v)
    edges[v].append(u)

make_tree(r,-1) #루트는 r번이고 루트의 부모는 없다(-1)
treedp(r)

for _ in range(q):
    
    u = int(stdin.readline())

    print(dp[u])

"""

from sys import stdin,setrecursionlimit
setrecursionlimit(1000000)

def dfs(u):
    
    for v in tree[u]:
        
        if visited[v] == 0:
            
            visited[v] = 1
            dfs(v)
            
            #DFS가 끝났다면 부모 정점의 정점 수 DP[u]에 현재 자식 v의 정점 수 DP[v]를 더해나간다
            #방문이 끝나고 나서 visited[v] = 0으로 하지 않는다
            
            dp[u] += dp[v]


n,r,q = map(int,stdin.readline().split())

tree = [[] for _ in range(n+1)]

#dp[u]는 u를 루트로 하는 서브트리에서 포함하는 정점의 수
#모든 서브트리는 루트 1개를 반드시 포함하니 1부터 시작
dp = [1]*(n+1) 

visited = [0]*(n+1)

for _ in range(n-1):
    
    u,v = map(int,stdin.readline().split())

    tree[u].append(v)
    tree[v].append(u)

visited[r] = 1 #루트부터 탐색 시작
dfs(r)

for _ in range(q):
    
    u = int(stdin.readline())

    print(dp[u])

"""