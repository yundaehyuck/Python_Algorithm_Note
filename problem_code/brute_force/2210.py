from sys import stdin

def dfs(x,y,maps,s,num):
    
    global num_set

    if s == 5:
        
        num_set.add(num)
    
    else:

        for nx,ny in [[0,1],[1,0],[0,-1],[-1,0]]:
            
            dx = x + nx
            dy = y + ny

            if dx >= 0 and dx <= 4 and dy >= 0 and dy <= 4:

                dfs(dx,dy,maps,s+1,num+str(maps[dy][dx]))

maps = [list(map(int,stdin.readline().split())) for _ in range(5)]

num_set = set()

for y in range(5):
    
    for x in range(5):

        dfs(x,y,maps,0,str(maps[y][x]))

print(len(num_set))