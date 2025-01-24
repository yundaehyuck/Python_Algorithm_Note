from collections import deque
from sys import stdin

#최초 루머 유포자가 루머를 퍼뜨리는데
#주변 정점 중 절반 이상이 루머를 믿으면 자신도 루머를 믿는다
#각 정점이 최초로 루머를 믿게 되는 시점을 찾는다

n = int(stdin.readline())

graph = [[] for _ in range(n+1)]

for i in range(1,n+1):

    A = list(map(int,stdin.readline().split()))
    
    for j in range(len(A)-1):

        graph[i].append(A[j])

m = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

answer = [-1]*(n+1) #정점들이 루머를 믿게 되는 시간
visited = [0]*(n+1) #방문 처리
count = [0]*(n+1) #주변 정점중 루머를 믿는 정점의 수

#최초 루머를 믿는 유포자부터 시작
queue = deque([])

for i in range(m):
    
    answer[A[i]] = 0
    queue.append(A[i])
    visited[A[i]] = 1

c = 0

while queue:
    
    z = len(queue)

    c += 1

    #매 분마다 큐의 길이만큼 반복

    for _ in range(z):
    
        x = queue.popleft()

        #루머를 믿고 있는 정점이 방문할 수 있는 주변 정점에 루머를 퍼뜨린다
        #이때 각 정점은 루머를 몇개나 받아들였는지 카운팅
        #즉 count[v]는 v 정점 주변에서 루머를 믿고 있는 정점의 수
        for v in graph[x]:
        
            if visited[v] == 0:
                
                count[v] += 1
                
                #이 때 루머를 믿고 있는 정점의 수가 주변 정점의 수 절반 이상이면, 그 정점은 루머를 믿게 된다
                #그래서 방문처리하고 큐에 넣어줌
                if count[v] >= len(graph[v])/2:
                    
                    queue.append(v)
                    visited[v] = 1
                    answer[v] = c
                    
print(*answer[1:])