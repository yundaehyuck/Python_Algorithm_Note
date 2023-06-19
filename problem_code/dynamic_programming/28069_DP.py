n,k = map(int,input().split())

INF = 1000000000000000000000000000000

dp = [INF for _ in range(n+1)]
dp[0] = 0

for i in range(n):
    
    dp[i+1] = min(dp[i]+1,dp[i+1])

    if i+i//2 <= n:
        
        dp[i+i//2] = min(dp[i]+1,dp[i+i//2])

if dp[n] <= k:
    
    print("minigimbob")

else:
    
    print("water")