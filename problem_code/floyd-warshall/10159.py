#i에서 j로 갈 수 있는가? j에서 i로 갈 수 있는가?

from sys import stdin

INF = 10000000000000000

def floyd(graph):

    for i in range(1,n+1):

        graph[i][i] = 0

    for k in range(1,n+1):

        for i in range(1,n+1):

            for j in range(1,n+1):

                if graph[i][j] > graph[i][k] + graph[k][j]:

                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph    

n = int(stdin.readline())

m = int(stdin.readline())

graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    
    i,j = map(int,stdin.readline().split())

    graph[i][j] = 1

graph = floyd(graph)

for i in range(1,n+1):
    
    count = 0

    for j in range(1,n+1):
        
        if graph[i][j] == INF and graph[j][i] == INF:
            
            count += 1
    
    print(count)