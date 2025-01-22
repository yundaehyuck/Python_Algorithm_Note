#일직선 위 n개의 샘터가 있을 때 가장 가까운 샘터까지 거리의 합이 최소가 되도록 k채의 집을 짓는 문제  
from collections import deque

n,k = map(int,input().split())

A = list(map(int,input().split()))

visited = {}
queue = deque([])

#(샘터 위치, 샘터까지 거리)를 모두 큐에 넣고
for i in range(n):
    
    visited[A[i]] = 0
    queue.append((A[i],0))

count = 0
v = 0

while queue:
    
    x,c = queue.popleft()
    
    #현재 위치에서 왼쪽 -1, 오른쪽 +1 부분을 확인
    #비어있으면 집을 짓고 샘터까지 거리 c+1를 누적해줌
    #집을 짓는데 성공하면 1씩 counting해서 총 k개 지으면 끝
    if visited.get(x-1,-1) == -1:
        
        visited[x-1] = 1
        v += c+1
        queue.append((x-1,c+1))
        count += 1
    
    if count == k:
        
        break

    if visited.get(x+1,-1) == -1:
        
        visited[x+1] = 1
        v += c+1
        queue.append((x+1,c+1))
        count += 1
    
    if count == k:
        
        break

print(v)