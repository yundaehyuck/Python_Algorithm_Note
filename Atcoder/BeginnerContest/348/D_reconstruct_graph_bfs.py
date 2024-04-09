from collections import deque
from sys import stdin

def bfs1(x,y,e,i):
    
    queue = deque([(x,y,e)])
    visited = [[0]*w for _ in range(h)]
    visited[y][x] = 1

    while queue:
        
        x,y,e = queue.popleft()

        if e > 0:

            for a,b in [[0,1],[1,0],[0,-1],[-1,0]]:
                
                dx = x + a
                dy = y + b

                if dx >= 0 and dx <= w-1 and dy >= 0 and dy <= h-1 and visited[dy][dx] == 0 and maps[dy][dx] != '#':
                    
                    if e-1 >= 0:
                        #에너지가 남아있을때, 약이 있는 위치에 이동할 수 있기만 한다면..
                        if med.get((dx,dy),0) != 0:
                            
                            graph[i].append(med[(dx,dy)][1])

                        queue.append((dx,dy,e-1))
                        visited[dy][dx] = 1

def bfs2(s,t,m,graph):
    
    queue = deque([s])

    visited = [0]*m
    visited[s] = 1

    while queue:
        
        s = queue.popleft()

        for v in graph[s]:
            
            if visited[v] == 0:
                
                if v == t:
                    
                    return True

                queue.append(v)
                visited[v] = 1
    
    return False

h,w = map(int,stdin.readline().split())

maps = [list(stdin.readline().rstrip()) for _ in range(h)]

#시작점, 도착점 찾기
for y in range(h):
    
    for x in range(w):
        
        if maps[y][x] == 'S':
            
            s_x = x
            s_y = y
        
        elif maps[y][x] == 'T':
            
            t_x = x
            t_y = y

n = int(stdin.readline())

med = {}

#모든 약의 위치를 찾기
s = -1 #시작점에 약이 있는가?
t = -1 #도착점에 약이 있는가?

for i in range(n):
    
    r,c,e = map(int,stdin.readline().split())

    if s_x == c-1 and s_y == r-1:
        
        s = i 
    
    if t_x == c-1 and t_y == r-1:
        
        t = i

    med[(c-1,r-1)] = (e,i)

if s == -1: #S = -1이면 시작점에 약이 없으니..
    
    print('No')

else:
    
    m = n

    if t == -1: #도착점에 약이 없는 경우...
        
        med[(t_x,t_y)] = (0,n)
        m = n+1
        t = n
    
    graph = [[] for _ in range(m)]
    
    #m개의 약 노드들에서, i번째 위치에서 먹은 약만으로
    #다른 노드로 갈 수 있는가?
    for x,y in med.keys():
        
        e,i = med[(x,y)]

        if e > 0:
            
            bfs1(x,y,e,i)
    
#그래프를 만들고, 해당 그래프 위에서
    #시작점에서 끝점으로 도달할 수 있는지 BFS
    if bfs2(s,t,m,graph):
        
        print('Yes')
    
    else:
        
        print('No')