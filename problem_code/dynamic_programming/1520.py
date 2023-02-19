from sys import stdin

def dfs(x,y,n,m,maps):
    
    if x == n-1 and y == m-1:

        return 1
    
    else:
        
        if dp[y][x] == -1:
            
            dp[y][x] = 0

            for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
                
                dx = x + ni
                dy = y + nj

                if dx >= 0 and dx <= n-1 and dy >= 0 and dy <= m-1:
                    
                    if maps[y][x] > maps[dy][dx]:
                        
                        dp[y][x] += dfs(dx,dy,n,m,maps)
        
        return dp[y][x]

m,n = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(m)]

dp = [[-1]*n for _ in range(m)]

dp[0][0] = dfs(0,0,n,m,maps)

print(dp[0][0])