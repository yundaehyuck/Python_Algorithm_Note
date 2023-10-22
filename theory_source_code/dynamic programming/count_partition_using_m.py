#m개 이하의 1,2,3을 중복해서 사용해 n을 만드는 경우의 수
#순서가 다르면 다른 경우의 수로 센다
from sys import stdin

mod = 1000000009

dp = [[0]*(1001) for _ in range(1001)]

dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

#dp[i-1][j-1] 각각에 1을 붙여주고
#dp[i-2][j-1] 각각에 2를 붙여주고
#dp[i-3][j-1] 각각에 3을 붙여주고
#이들을 모두 더해주면 j개의 수로 i를 만드는 경우의 수
#순서가 다르면 다른 경우의 수로 세니 n = 1~1000을 먼저 순회함

for i in range(4,1001):
    
    for j in range(1,i+1):
                    
        dp[i][j] += (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1])
        dp[i][j] %= mod

T = int(stdin.readline())

for _ in range(T):
    
    n,m = map(int,stdin.readline().split())
    
    answer = 0
    
    #dp[n][i] = i개의 수를 사용해 n을 만드는 경우의 수
    #dp[n][1] + dp[n][2] + ... + dp[n][m] = m개 이하의 수를 사용해 n을 만드는 경우의 수
    for i in range(1,m+1):
        
        answer += dp[n][i]
        answer %= mod
    
    print(answer)