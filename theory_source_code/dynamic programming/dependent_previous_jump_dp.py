#이전에 x칸 점프하면 현재 x-1,x,x+1칸 중 하나 점프할 수 있을때
#1번에서 n번까지 점프한 최소 횟수
#특정 칸은 점프 불가
from sys import stdin

n,m = map(int,stdin.readline().split())

A = [0]*(n+1)

for _ in range(m):

    m = int(stdin.readline())
    A[m] = 1 #점프가 불가능한 곳을 표시

#dp[i][j] = i번째 칸에 j칸 점프해서 올때 최소 점프 횟수
#x = 1부터 시작해서 1+2+...+m <=10000인 m을 찾으면 m = 140정도도
dp = [[0]*145 for _ in range(n+1)]

if A[2] == 1:

    dp[2][1] = 0

else:
    
    dp[2][1] = 1

#x-1칸 점프하면 dp[i+x-1][x-1] = dp[i][x]+1
#x칸 점프하면 dp[i+x][x] = dp[i][x] + 1
#x+1칸 점프하면 dp[i+x+1][x+1] = dp[i][x]+1
#이때 i+x-1,i+x,i+x+1에 점프할 수 있는지 아닌지 체크해야함
for i in range(2,n+1):
    
    for x in range(1,143):
        
        if dp[i][x] > 0:
            
            if i+x <= n and A[i+x] == 0:
                
                dp[i+x][x] = dp[i][x] + 1
            
            if i+x-1 <= n and A[i+x-1] == 0:
                
                dp[i+x-1][x-1] = dp[i][x] + 1
            
            if i+x+1 <= n and A[i+x+1] == 0:
                
                dp[i+x+1][x+1] = dp[i][x] + 1

#몇칸으로 점프하든 n에 도달한 칸 dp[n][1],...,dp[n][142]중 최솟값
INF = 10**18
answer = INF

for i in range(143):

    if dp[n][i] > 0:
        
        if answer > dp[n][i]:
            
            answer = dp[n][i]

if answer == INF:
    
    answer = -1
    
print(answer)