#BOJ 24463
from collections import deque
from sys import stdin

#순방향 bfs
#출구까지 가는 최단 경로 길이를 visited에 표시
def bfs(x,y,z,w,n,m,maze):
    
    visited = [[0]*m for _ in range(n)]

    visited[y][x] = 1

    queue = deque([(x,y)])

    while queue:
        
        x,y = queue.popleft()

        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            
            dx = x + ni
            dy = y + nj

            if dx >= 0 and dx <= m-1 and dy >= 0 and dy <= n-1 and visited[dy][dx] == 0 and maze[dy][dx] == '@':
                
                visited[dy][dx] = visited[y][x] + 1

                if dx == z and dy == w:
                    
                    return visited
                
                else:
                    
                    queue.append((dx,dy))

#최단 경로 역추적 bfs

def bfs_tracking(z,w,x,y,n,m,maze,visited):
    
    queue = deque([(z,w)])

    while queue:
        
        z,w = queue.popleft()

        maze[w][z] = '.' #이동하면서 .으로 표시

        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            
            dz = z + ni
            dw = w + nj

            #배열의 범위는 벗어나지 말아야하고 @인 부분만 이동 가능함

            if dz >= 0 and dz <= m-1 and dw >= 0 and dw <= n-1 and maze[dw][dz] == '@':
                
                #z,w에서 visited값보다 1 적은 곳으로만 이동 가능하다
                if visited[dw][dz] == visited[w][z] - 1:
                    
                    queue.append((dz,dw))
              
n,m = map(int,stdin.readline().split())

maze = [list(stdin.readline().rstrip()) for _ in range(n)]

#이동할 수 있는 .을 @로 바꿔놓는다

for y in range(n):
    
    for x in range(m):
        
        if maze[y][x] == '.':
            
            maze[y][x] = '@'

#가장자리를 조사해서 입구와 출구를 찾는다
#.은 @로 바뀌었다

start = []

for y in range(n):
    
    if y == 0 or y == n-1:
        
        for x in range(m):

            if maze[y][x] == '@':

                start.append((x,y))

    else:

        if maze[y][0] == '@':

            start.append((0,y))

        elif maze[y][m-1] == '@':

            start.append((m-1,y))

#bfs 수행

x,y = start[0][0],start[0][1]
z,w = start[1][0], start[1][1]

visited = bfs(x,y,z,w,n,m,maze)

#최단 경로 역추적
bfs_tracking(z,w,x,y,n,m,maze,visited)

for row in maze:
    
    print(''.join(row))