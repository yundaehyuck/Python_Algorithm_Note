from collections import deque
from sys import stdin

def bfs(s_x,s_y,g_x,g_y,r,c,maps,water_list):
    
    visited = [[0]*c for _ in range(r)]

    queue = deque([(s_x,s_y)])

    visited[s_y][s_x] = 1

    while queue:

        len_w = len(water_list)

        for _ in range(len_w):

            w_x,w_y = water_list.popleft()

            for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
                
                d_w_x = w_x+ni
                d_w_y = w_y+nj

                if d_w_x >= 0 and d_w_x <= c-1 and d_w_y >= 0 and d_w_y <= r-1 and (maps[d_w_y][d_w_x] == '.' or maps[d_w_y][d_w_x] == 'S'):

                    maps[d_w_y][d_w_x] = '*'

                    water_list.append((d_w_x,d_w_y))
        
        len_s = len(queue)

        for _ in range(len_s):

            x,y = queue.popleft()

            for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
                
                dx = x + ni
                dy = y + nj

                if dx >= 0 and dx <= c-1 and dy >= 0 and dy <= r-1 and maps[dy][dx] != '*' and maps[dy][dx] != 'X' and visited[dy][dx] == 0:
                    
                    queue.append((dx,dy))

                    visited[dy][dx] = visited[y][x] + 1

                    if dx == g_x and dy == g_y:
                        
                        return visited[dy][dx]-1
    
    return 'KAKTUS'
        


r,c = map(int,stdin.readline().split())

maps = [list(stdin.readline()) for _ in range(r)]

water_list = deque([])

for y in range(r):
    
    for x in range(c):
        
        if maps[y][x] == 'S':
            
            s_x = x
            s_y = y
        
        elif maps[y][x] == 'D':
            
            g_x = x
            g_y = y
        
        elif maps[y][x] == '*':
            
            water_list.append((x,y))

print(bfs(s_x,s_y,g_x,g_y,r,c,maps,water_list))