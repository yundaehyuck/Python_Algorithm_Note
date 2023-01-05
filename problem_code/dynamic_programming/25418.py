from sys import stdin

dp = [100000000]*(1000001)

a,k = map(int,stdin.readline().split())

dp[a] = 0

for i in range(a+1,k+1):
    
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        
        dp[i] = min(dp[i],dp[i//2] + 1)

print(dp[k])