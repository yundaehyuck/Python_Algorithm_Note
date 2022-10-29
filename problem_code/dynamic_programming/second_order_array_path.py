#https://www.acmicpc.net/problem/17070
#https://www.acmicpc.net/problem/17069
from sys import stdin

n = int(stdin.readline())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

#i=0 가로
#i=1 세로
#i=2 대각선으로 (x,y)지점에 가는 방법의 수

dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]


#초기 상태, (1,0)에 가로로 1가지 가능

dp[0][1][0] = 1

#문제 조건에 의해, x는 2~n-1, y는 0~n-1인 영역만 파이프가 존재할 수 있다
for y in range(n):
    
    for x in range(2,n):
        
        ##가로로 들어오는 경우와 세로로 들어오는 경우를 센다
        ##애초에 (x,y)가 벽이면 (x,y)에는 파이프가 들어갈 수가 없다
        if maps[y][x] == 1:
            
            continue
        
        #가로(0)으로 들어가는 방법의 수
        dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]
        #세로(1)로 들어가는 방법의 수
        dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]
        
        #대각선으로 들어오는 경우를 센다
        #(x,y-1)과 (x-1,y)가 벽이 아니어야 대각선으로 (x,y)에 들어갈 수 있다
        if maps[y-1][x] == 1 or maps[y][x-1] == 1:
            
            continue
        
        #(x,y)에 대각선으로 들어가는 방법의 수
        
        dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]


#for문을 전부 돌아 dp배열을 채우면.. (n-1,n-1)에 경우의 수가 존재함
print(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2])