from collections import deque
from sys import stdin

#https://www.acmicpc.net/problem/2206

def bfs(x,y,z,n,m,maps):
    
    if n == 1 and m == 1:
        
        return 1
    
    else:
    
        visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

        visited[y][x][z] = 1

        queue = deque([(x,y,z)])

        while queue:

            x,y,z = queue.popleft()

            for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:

                dx = x + ni
                dy = y + nj

                if dx >= 0 and dx <= m-1 and dy >= 0 and dy <= n-1:

                    if z == 0:

                        if maps[dy][dx] == '1' and visited[dy][dx][z+1] == 0:

                            visited[dy][dx][z+1] = visited[y][x][z] + 1

                            queue.append((dx,dy,z+1))

                            if dx == m-1 and dy == n-1:

                                return visited[dy][dx][z+1]

                        elif maps[dy][dx] == '0' and visited[dy][dx][z] == 0:

                            visited[dy][dx][z] = visited[y][x][z] + 1

                            queue.append((dx,dy,z))


                            if dx == m-1 and dy == n-1:

                                return visited[dy][dx][z]


                    else:

                        if visited[dy][dx][z] == 0 and maps[dy][dx] == '0':

                            visited[dy][dx][z] = visited[y][x][z] + 1

                            queue.append((dx,dy,z))


                            if dx == m-1 and dy == n-1:

                                return visited[dy][dx][z]

        return -1
        
    
n,m = map(int,stdin.readline().split())

maps = [list(stdin.readline()) for _ in range(n)]

print(bfs(0,0,0,n,m,maps))