#합이 k가 되는 경우의 수를 세는 방법
#구성이 같은데, 순서가 달라도 같은 경우로 세는 경우의 수
from sys import stdin

dp = [0]*10001

dp[0] = 1

#사용하는 도구 1,2,3 먼저 돌고
#모든 n에 대해 돌아야 순서가 달라도 같은 경우로 센다
for i in range(1,4):
    
    for j in range(1,10001):
        
        if j - i >= 0:
            
            dp[j] += dp[j-i]

T = int(stdin.readline())

for _ in range(T):
    
    n = int(stdin.readline())

    print(dp[n])