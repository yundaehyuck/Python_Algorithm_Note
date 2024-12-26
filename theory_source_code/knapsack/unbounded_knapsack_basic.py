#무한 냅색
#dp[i] = min(dp[i], dp[i-k*W[j]] + k*V[j]) = min(dp[i], dp[i-W[j]] + V[j])

n = 120

dp = [0]*(n+1)

dp[1] = 1

for i in range(2,n+1):
    
    dp[i] = dp[i-1] + i

for i in range(2,n+1):
    
    dp[i] += dp[i-1]

N = int(input())

INF = 10**12

dp2 = [INF]*(N+1)
dp2[0] = 0
    
for i in range(1,n+1):
    
    for j in range(dp[i],N+1): #핵심은 가방의 무게는 정방향 j = 1,2,3,...,N으로 순회해야함
        
        dp2[j] = min(dp2[j], dp2[j-dp[i]] + 1)

"""
for i in range(1,n+1):
    
    for j in range(dp[i], N+1):
        
        for k in range(1,j//dp[i]+1):
            
            dp2[j] = min(dp2[j], dp2[j-k*dp[i]] + k)
"""

print(dp2[N])