#cycling connected component 

from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

visited = [0]*(n+1)
degree = [0]*(n+1)

#그래프를 만들때, 연결차수도 구해준다.
for _ in range(m):
    
    a,b,c,d = input().split()

    a = int(a)
    c = int(c)
    
    graph[a].append(c)
    graph[c].append(a)

    degree[a] += 1
    degree[c] += 1

#1번부터 N번까지 BFS수행
cycle = 0
no_cycle = 0

for i in range(1,n+1):
    
    if visited[i] == 0:
        
        queue = deque([i])

        visited[i] = 1
         
        flag = True #연결요소의 cycle이 존재한다.

        while queue:
            
            x = queue.popleft()
            
            #방문한 정점이 연결차수가 2가 아니라면,
            #해당 정점을 포함하는 연결요소는 사이클이 없다
            if degree[x] != 2:
                
                flag = False
            
            for v in graph[x]:
                
                if visited[v] == 0:
                    
                    queue.append(v)
                    visited[v] = 1
        
        #정점 i를 포함하는 연결요소를 만들고 나서, flag=True라면
        #해당 연결요소의 모든 정점은 연결차수가 2이다.
        #그래서 사이클이 존재함
        if flag == True:
            
            cycle += 1
        
        else:
            
            no_cycle += 1

print(cycle, no_cycle)