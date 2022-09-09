#https://www.acmicpc.net/problem/2667

from sys import stdin

def dfs(x,y,n):
    
    global d,maps
    
    maps[y][x] = '0'
    
    d += 1

    for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
    
        dx = x + ni
        dy = y + nj

        if dx >= 0 and dy >= 0 and dx <= n-1 and dy <= n-1 and maps[dy][dx] == '1':
            
            dfs(dx,dy,n)
                

n = int(stdin.readline())

maps = [list(stdin.readline().rstrip()) for _ in range(n)]

ans = 0

cnt_list = []

for y in range(n):
    
    for x in range(n):
        
        d = 0

        if maps[y][x] != '0':
        
            dfs(x,y,n)

        if d != 0:
            
            ans += 1
            cnt_list.append(d)

cnt_list.sort()

print(ans)

for cnt in cnt_list:
    
    print(cnt)