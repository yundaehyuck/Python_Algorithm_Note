#(0,0) 에서 (n,n)까지 동쪽 혹은 남쪽으로만 가면서 우유를 마실때 최대로 마실 수 있는 우유의 개수
#맨 처음에는 딸기 우유
#딸기 우유 마시고 나서는 초코우유
#초코우유 마시고 나서는 바나나우유
#바나나우유 마시고 나서는 딸기우유
from sys import stdin

n = int(stdin.readline())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

#dp[i][j][k] = (j,i)에서 마지막으로 k번째 우유를 마실때 그 동안 최대로 마신 우유의 개수
dp = [[[0]*3 for _ in  range(n)] for _ in range(n)]

#맨 처음에 딸기 우유를 마신다
#초기화
#일단 딸기우유인 곳에서 dp[y][x][0] = 1로 해두고

for y in range(n):
    
    for x in range(n):
        
        if maps[y][x] == 0:
            
            dp[y][x][0] = 1

#y = 0일때 x방향으로 초기화

for x in range(1,n):
    
    for i in range(3):
        
        dp[0][x][i] = max(dp[0][x][i],dp[0][x-1][i]) #우유를 마시지 않는 경우
    
    #우유를 마시는 경우

    if maps[0][x] == 0:
        
        if dp[0][x-1][2] >= 1: #dp[0][x-1][2] >= 1이어야함. = 0인 경우는 처음에 딸기우유를 안마셨으니 안됨

            dp[0][x][0] = max(dp[0][x][0],dp[0][x-1][2] + 1)
    
    elif maps[0][x] == 1:
        
        if dp[0][x-1][0] >= 1:

            dp[0][x][1] = max(dp[0][x][1],dp[0][x-1][0] + 1)
    
    else:
        
        if dp[0][x-1][1] >= 1:

            dp[0][x][2] = max(dp[0][x][2],dp[0][x-1][1] + 1)


#x = 0인 경우 y방향 초기화
for y in range(1,n):
    
    for i in range(3):
            
        dp[y][0][i] = max(dp[y][0][i], dp[y-1][0][i])
    
    if maps[y][0] == 0:
        
        if dp[y-1][0][2] >= 1:

            dp[y][0][0] = max(dp[y][0][0], dp[y-1][0][2] + 1)
    
    elif maps[y][0] == 1:
        
        if dp[y-1][0][0] >= 1:

            dp[y][0][1] = max(dp[y][0][1], dp[y-1][0][0] + 1)
    
    else:
        
        if dp[y-1][0][1] >= 1:

            dp[y][0][2] = max(dp[y][0][2], dp[y-1][0][1] + 1)

#(1,1)에서 (n-1,n-1)까지 계산
for y in range(1,n):
    
    for x in range(1,n):
        
        #우유를 안마시는 경우 동쪽 남쪽에서 와야하므로
        #dp[y][x][i] = dp[y][x-1][i], dp[y-1][x][i]중 최댓값
        for i in range(3):
                
            dp[y][x][i] = max(dp[y][x][i], dp[y][x-1][i], dp[y-1][x][i])
        
        #우유를 마시는 경우
        #dp[y][x][0] = max(dp[y-1][x][2] + 1, dp[y][x-1][2] + 1)
        #근데 dp[y-1][x][2] >= 1, dp[y][x-1][2] >= 1이어야함
        # = 0인 경우는 맨 처음에 딸기 우유를 안마신거
        if maps[y][x] == 0:
            
            if dp[y-1][x][2] >= 1:

                dp[y][x][0] = max(dp[y-1][x][2] + 1, dp[y][x][0])
            
            if dp[y][x-1][2] >= 1:
                
                dp[y][x][0] = max(dp[y][x-1][2] + 1, dp[y][x][0])

        elif maps[y][x] == 1:
            
            if dp[y][x-1][0] >= 1:

                dp[y][x][1] = max(dp[y][x-1][0] + 1, dp[y][x][1])
            
            if dp[y-1][x][0] >= 1:
                
                dp[y][x][1] = max(dp[y-1][x][0] + 1, dp[y][x][1])

        elif maps[y][x] == 2:
            
            if dp[y][x-1][1] >= 1:

                dp[y][x][2] = max(dp[y][x-1][1] + 1, dp[y][x][2])
            
            if dp[y-1][x][1] >= 1:
                
                dp[y][x][2] = max(dp[y-1][x][1] + 1, dp[y][x][2])

print(max(dp[n-1][n-1]))
