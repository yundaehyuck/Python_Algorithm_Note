#2차원 배열 누적합
from sys import stdin

n,m = map(int,stdin.readline().split())

matrix = [list(map(int,stdin.readline().split())) for _ in range(n)]

#dp[y][x] = 좌상단 (0,0) 우하단 (x,y)까지 사각형의 모든 원소의 합
dp = [[0]*(n+1) for _ in range(n+1)]

#dp[y][x] = dp[y-1][x] + dp[y][x-1] + matrix[y][x] - dp[y-1][x-1]
#x = 0이거나 y = 0인 경우 해당 dp값은 0으로 처리
dp[0][0] = matrix[0][0]

for y in range(1,n):
    
    dp[y][0] = matrix[y][0] + dp[y-1][0]

for x in range(1,n):
    
    dp[0][x] = matrix[0][x] + dp[0][x-1]

for y in range(1,n):
    
    for x in range(1,n):
        
        dp[y][x] = dp[y-1][x] + dp[y][x-1] + matrix[y][x] - dp[y-1][x-1]

#(x1,y1)~(x2,y2)까지의 합은..
#dp[y2][x2] - dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1]
#역시 x1 = 0 이거나 y1 = 0인 경우 해당 dp는 0으로 처리
for _ in range(m):
    
    y1,x1,y2,x2 = map(int,stdin.readline().split())

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    A = dp[y2][x2]

    if y1 == 0:
        
        B = 0
    
    else:
        
        B = dp[y1-1][x2]
    
    if x1 == 0:
        
        C = 0
    
    else:
        
        C = dp[y2][x1-1]
    
    if x1 == 0 and y1 == 0:
        
        D = 0
    
    else:
        
        D = dp[y1-1][x1-1]

    print(A - B - C + D)