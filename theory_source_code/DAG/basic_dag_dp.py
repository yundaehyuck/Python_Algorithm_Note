#DAG위에서 DP
#각 정점까지 도달하는데 걸리는 최소 시간

from collections import deque
from sys import stdin

#위상정렬
def topology_sort(graph,indegree,n):
    
    queue = deque([])
    
    #들어오는 간선의 개수가 0개인 노드들을 모두 큐에 넣는다.
    for i in range(1,n+1):
        
        if indegree[i] == 0:
            
            queue.append(i)
    
    order = []

    while queue:
        
        u = queue.popleft() #노드 하나를 빼고,

        order.append(u) #정렬 결과 배열에 넣어준 다음,

        for v in graph[u]: #u와 연결된 노드 v에 대하여...
            
            indegree[v] -= 1 #u를 제거했으므로 v의 들어오는 간선의 개수는 1씩 감소

            if indegree[v] == 0: #이때, v의 들어오는 간선의 개수가 0개가 된다면...
                
                queue.append(v) #큐에 넣어준다
    
    return order

def solve(D,graph,order,w,n):
    
    dp = [0]*(n+1)

    for u in order: #위상정렬 순서대로 순회해서...
        
        if dp[u] < D[u-1]:
            
            dp[u] = D[u-1] #각 정점 u의 건설시간의 시작 시간을 dp[u] = max(dp[u],d[u-1])로 초기화
        
        for v in graph[u]: #v로 들어올 수 있는 모든 u에 대하여...
            
            #이전에 건설된 시간 dp[u]에 해당 정점 v의 건설시간 d[v-1]을 더한게 dp[v]
            #가능한 dp[v]중 최댓값으로 저장
            if dp[u]+D[v-1] > dp[v]:
                
                dp[v] = dp[u]+D[v-1]
    
    return dp[w] #w까지 건설하는데 걸리는 최소시간이 답

T = int(stdin.readline())

for _ in range(T):
    
    n,k = map(int,stdin.readline().split())

    D = list(map(int,stdin.readline().split()))

    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1) #각 노드의 들어오는 간선의 개수

    for _ in range(k):
        
        u,v = map(int,stdin.readline().split())

        graph[u].append(v) 
        
        #u에서 v로 이동하는 간선이 존재한다면, v의 들어오는 간선의 개수 1 증가
        indegree[v] += 1
    
    w = int(stdin.readline())

    order = topology_sort(graph,indegree,n)

    print(solve(D,graph,order,w,n))