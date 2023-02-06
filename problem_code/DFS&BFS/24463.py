from sys import stdin
import sys

sys.setrecursionlimit(50000)

def dfs(x,y,z,w,n,m,maze):
    
    if x == z and y == w:
        
        return True
    
    else:

        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            
            dx = x + ni
            dy = y + nj

            if dx >= 0 and dy >= 0 and dx <= m-1 and dy <= n-1 and maze[dy][dx] == '@':
                
                maze[dy][dx] = '.'

                find = dfs(dx,dy,z,w,n,m,maze)

                if find:
                    
                    return True

                maze[dy][dx] = '@'
        
        return False
         
n,m = map(int,stdin.readline().split())

maze = [list(stdin.readline().rstrip()) for _ in range(n)]

start_target = []

for y in range(n):
    
    for x in range(m):
        
        if maze[y][x] == '.':
            
            maze[y][x] = '@'

for y in range(n):
    
    if y == 0 or y == n-1:
        
        for x in range(m):
            
            if maze[y][x] == '@':
                
                start_target.append((x,y))
    
    else:
        
        if maze[y][0] == '@':
            
            start_target.append((0,y))
        
        elif maze[y][m-1] == '@':
            
            start_target.append((m-1,y))

x,y = start_target[0]
z,w = start_target[1]

maze[y][x] = '.'

dfs(x,y,z,w,n,m,maze)

for row in maze:
    
    print(''.join(row))