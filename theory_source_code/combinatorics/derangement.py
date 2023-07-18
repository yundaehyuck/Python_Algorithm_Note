mod = 1000000000

n = int(input())

dp = [0]*(n+1)

#교란순열
#자기 자신 것을 다시 갖지 않고 나눠주는 경우의 수
#a[0] = 0, a[1] = 0, a[2] = 1, a[n] = (n-1)(a[n-1]+a[n-2])

if n >= 2:
    
    dp[2] = 1

for i in range(3,n+1):

    dp[i] = (i-1)*(dp[i-1]+dp[i-2])
    dp[i] %= mod

print(dp[n] % mod)