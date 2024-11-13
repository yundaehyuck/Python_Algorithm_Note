#사이클이 하나 있는 무방향 연결그래프에서 각 노드에서 사이클까지 최소 거리

from collections import deque

n = int(input())

graph = [set() for _ in range(n)] #set으로 구현하면 노드번호 제거할때 O(1)에 가능

for _ in range(n):
    
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

#무방향 연결그래프니까 진입차수가 0이 아니라 1인 노드를 큐에 담는다
#인접한 노드의 수가 1인 노드를 큐에 모두 담는다
queue = deque([])

for i in range(n):
    
    if len(graph[i]) == 1:
        
        queue.append(i)
        
adj = [0]*n #adj[i]는 i번 노드에 가장 인접한 노드
s = [] #위상정렬 노드

while queue:
    
    i = queue.popleft()
    s.append(i)
    
    for j in graph[i]:
        
        adj[i] = j #i번 노드에 인접한 노드는 j번
        
        graph[j].remove(i) #j번에서 i번을 제거하고
        
        if len(graph[j]) == 1: #제거했더니 j번 노드에 인접한 노드수가 1이면
            
            queue.append(j) #j번을 큐에 담아주고
        
    graph[i].pop() #i번에 인접한 노드는 1개니까 그 1개를 pop()으로 제거

#answer[i] = i번 노드에서 사이클까지 최소 거리
answer = [0]*n

#위상정렬 결과를 역방향으로 순회하면, 사이클에서 가장 가까운 노드부터 순회하게 됨
#위상정렬하면 사이클에 있는 노드는 s에 담기지 않는다
#그래서 사이클에서 가장 가까운 노드부터 거리가 1씩 증가하게 된다
for i in s[::-1]:
    
    answer[i] = answer[adj[i]] + 1

print(*answer)