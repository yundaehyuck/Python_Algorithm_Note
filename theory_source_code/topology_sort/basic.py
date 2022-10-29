#위상정렬 알고리즘

from collections import deque

#노드의 개수와 간선의 개수

v,e = map(int,input().split())

#모든 노드에 대한 진입차수를 0으로 초기화함
#노드 번호는 1번부터 v번까지

indegree = [0]*(v+1)

#각 노드에 연결된 간선의 정보를 담는 연결리스트(그래프) 초기화

graph = [[] for _ in range(v+1)]

#방향 그래프의 모든 간선의 정보를 입력

for _ in range(e):
    
    a,b = map(int,input().split())

    graph[a].append(b) #정점 a에서 b로 이동가능하다

    #a에서 b로 이동하므로, b로 들어오는 간선의 개수가 1개 늘어났다.
    #b의 진입차수를 1 증가
    indegree[b] += 1

#위상 정렬 알고리즘
    
result = [] #알고리즘 수행 결과

q = deque() #deque로 삽입,삭제 빠르게

#처음 시작에는 진입차수가 0인 노드를 모두 큐에 넣는다.

for i in range(1,v+1):
    
    if indegree[i] == 0:
        
        q.append(i)


#큐가 빌 때까지
#큐에 노드 1개 꺼내고, 출발하는 간선 모두 제거하고, 새롭게 진입차수가 0인 노드를 큐에 넣고

#큐가 빌때까지 반복
while q:
    
    #큐에서 노드 1개 꺼내기
    now = q.popleft()

    #위상정렬 결과를 기록하기 위해
    result.append(now)
    
    #now와 연결된 정점을 모두 찾는다.
    for i in graph[now]:
        
        #now에서 출발하는 간선을 제거
        #now에서 i로 가는 간선을 하나 제거한다는 것은, 
        #i의 진입차수를 1 감소시킨다는 소리이다.

        indegree[i] -= 1

        #만약 진입차수가 0이 된다면... 큐에 i번 노드를 삽입한다
        if indegree[i] == 0:
            
            q.append(i)


#위상 정렬 결과

for i in result:
    
    print(i,end=' ')