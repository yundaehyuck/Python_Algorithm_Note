#BFS로 이분 그래프를 판별하는 알고리즘

from collections import deque

def bfs(v,group):
    
    queue = deque([v]) #BFS 큐 생성

    visited[v] = group #방문 처리로 현재 그룹 할당

    while queue:
        
        v = queue.popleft() #탐색 시작

        for w in graph[v]: #인접한 정점을 순회하면서..
            
            if visited[w] == 0: #아직 방문하지 않은 정점이라면...
                
                queue.append(w) #다음 방문을 수행하기 위해 큐에 담고

                visited[w] = -visited[v] #현재 정점과는 다른 색을 부여함
            
            elif visited[w] == visited[v]: #이미 방문한 정점이라면...
                
                return False #이분 그래프가 아니다
    
    return True #False를 return하지 않는다면 현재 점에서는 이분그래프 가능성이 있다

#정점의 수와 간선의 수를 입력받는다

v,e = map(int,input().split())

#정점이 1~v인 그래프를 생성

graph = [[] for _ in range(v+1)]

#방문 여부 체크하는 배열

visited = [0]*(v+1)

#간선을 입력받는다

for _ in range(e):
    
    a,b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)


#연결그래프와 비연결그래프를 모두 고려하여 
#모든 정점을 순회하면서 방문하지 않은 정점이라면
#방문을 시작

for i in range(1,v+1):
    
    if visited[i] == 0: #아직 방문하지 않은 정점이라면..
        
        bipartite = bfs(i,1) #bfs 탐색을 시작

        if bipartite == False: #이분 그래프가 아니라면
            
            break #반복 종료

print(bipartite)

"""
9 11
1 2
2 3
3 4
3 5
4 6
5 6
5 7
7 8
6 8
9 8
5 9
True
"""