from sys import stdin

dp = [0]*((10**6)+1)

dp[1] = 0

dp[2] = 1

dp[3] = 1

N = int(stdin.readline())

for n in range(4,N+1):
    
    dp[n] = 1 + dp[n-1]
    
    if n % 3 == 0:
        
        dp[n] = min(dp[n],dp[n//3]+1)
    
    if n % 2 == 0:
        
        dp[n] = min(dp[n],dp[n//2]+1)
        
print(dp[N])