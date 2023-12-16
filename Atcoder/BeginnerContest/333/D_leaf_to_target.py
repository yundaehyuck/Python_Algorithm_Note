from sys import stdin,setrecursionlimit
setrecursionlimit(500000)

#리프노드부터 시작해서 1번 노드를 지우기까지 최소 개수를 지우는 방법

#먼저 u를 루트로 하는 서브트리의 노드 개수를 모두 구한다
def dfs(u):
    
    dp[u] = 1
    
    for v in tree[u]:
        
        if visited[v] == 0:
            
            visited[v] = 1
            dfs(v)
            dp[u] += dp[v]

n = int(stdin.readline())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    
    u,v = map(int,stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [0]*(n+1)
visited[1] = 1

dp = [0]*(n+1)

dfs(1)

answer = 0

ind = -1
cost = 0

for v in tree[1]:
    
    if dp[v] > cost:
        
        cost = dp[v]
        ind = v

#1번에 연결된 자식 정점이 v1,v2,..,vn이라고 한다면...
#v1,v2,...,vn을 루트로 하는 서브트리의 노드 개수의 최댓값 max_v를 제외한
#나머지 노드들을 모두 지우고, 1번을 지우면 최소 개수만큼 지우게 된다.
#왜냐하면 max_v를 지운다면 어떻게 지우더라도 무조건 최소 개수를 넘어가게 된다.
for v in tree[1]:
    
    if v != ind:
        
        answer += dp[v]

print(answer+1)