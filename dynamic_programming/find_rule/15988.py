#https://www.acmicpc.net/problem/15988
from sys import stdin

T = int(stdin.readline())

div = 1000000009

dp = [0]*1000001

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,1000001):
    
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % div

for _ in range(T):
    
    n = int(stdin.readline())
    
    print(dp[n])