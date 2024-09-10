#그래프에서 서로 연결된 세 정점 a,b,c의 차수 합의 최솟값
from sys import stdin

n,m = map(int,stdin.readline().split())

graph = [set() for _ in range(n+1)] #set으로 관리해서 O(1)에 연결된 정점을 찾도록

for _ in range(m):

    a,b = map(int,stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

INF = 10**18

answer = INF

#1번부터 n번까지 a라고 하면
for a in range(1,n+1):
    
    if len(graph[a]) >= 2: #a에 연결된 정점 중 2가지를 선택해야하니, 최소 2 이상인 얘들만
        
        #graph[a]에는 a에 연결된 정점이 있으므로 a,b는 서로 연결
        for b in graph[a]:
            
            #(a,b,c)에 대하여 d(a) + d(b) + d(c)를 구하므로
            #(1,3,5)에 대해 구했다면
            #a = 3인 경우 (3,1,5)도 계산해야하므로, a < b < c 조건을 달면 중복 계산을 방지함
            if b > a: 
                
                for c in graph[b]: #graph[b]에는 b에 연결된 정점이 있으므로 b,c가 서로 연결

                    if c > b and c in graph[a]: #c in graph[a]를 하면 a와 c가 연결

                        v = len(graph[a]) + len(graph[b]) + len(graph[c]) - 6

                        if answer > v:

                            answer = v

if answer == INF:
    
    print(-1)

else:

    print(answer)