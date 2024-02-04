from collections import deque
from sys import stdin

def bfs(player,maps,n):
    
    visited = [[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]

    count = 0
    queue = deque()
    queue.append((player,count))

    INF = 1000000000000000000000000000000000
    answer = INF

    while queue:
        
        player,count = queue.popleft()
        
        if answer < count:
            continue

        x = 0
        y = 0
        z = 0
        w = 0

        for a,b,i in player:
            
            if i == 1:
                
                x = a
                y = b
            
            else:
                
                z = a
                w = b
        
        for a,b in [[0,1],[1,0],[0,-1],[-1,0]]:
            
            dx = x + a
            dy = y + b
            dz = z + a
            dw = w + b

            if dx < 0 or dx > n-1 or dy < 0 or dy > n-1 or maps[dy][dx] == '#':
                
                dx = x
                dy = y
            
            if dz < 0 or dz > n-1 or dw < 0 or dw > n-1 or maps[dw][dz] == '#':
                
                dz = z
                dw = w
            
            if visited[dx][dy][dz][dw] == 0:
                
                visited[dx][dy][dz][dw] = 1

                dcount = count + 1

                if dx == dz and dy == dw:
                    
                    if answer > dcount:
                        
                        answer = dcount
                
                else:

                    player = [(dx,dy,1),(dz,dw,2)]
                    queue.append((player,dcount))
    
    if answer == INF:
        
        answer = -1

    return answer

n = int(stdin.readline())

maps = [list(stdin.readline().rstrip()) for _ in range(n)]

player = []

i = 1

for y in range(n):
    
    for x in range(n):
        
        if maps[y][x] == 'P':
            
            player.append((x,y,i))
            i += 1

print(bfs(player,maps,n))