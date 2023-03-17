#2623 BOJ
from collections import deque
from sys import stdin

n,m = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)]

indegree = [0]*(n+1)

for _ in range(m):
    
    order_list = list(map(int,stdin.readline().split()))

    k = order_list[0]

    for i in range(1,k):
        
        graph[order_list[i]].append(order_list[i+1])

        indegree[order_list[i+1]] += 1

q = deque()

for i in range(1,n+1):
    
    if indegree[i] == 0:
        
        q.append(i)

result = []
count = 0

while q:
    
    now = q.popleft()

    result.append(now)
    count += 1 #결과 리스트에 들어가는 노드 수를 세준다

    for v in graph[now]:
        
        indegree[v] -= 1

        if indegree[v] == 0:
            
            q.append(v)

#큐가 빌때까지, 결과 리스트에 들어있는 노드 수가
#원래 노드 수 n보다 작다면, 모든 노드를 방문하지 못했다.
# 이런 경우는 위상정렬이 불가능하다.
# 그래프에 사이클이 존재한다.

if count < n:
    
    print(0)

else:
    
    for v in result:

        print(v)