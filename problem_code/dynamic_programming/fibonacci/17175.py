from sys import stdin

n = int(stdin.readline())

div = 1000000007

if n <= 1:
    
    print(1)

elif n == 2:
    
    print(3)

elif n == 3:
    
    print(5)

else:
    dp = [0]*(n+1)

    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5

    minus_dp = [0]*(n)

    minus_dp[0] = 1
    minus_dp[1] = 2
    minus_dp[2] = 2

    for i in range(3,n):
        
        minus_dp[i] = (minus_dp[i-1]+minus_dp[i-2])%div

        dp[i+1] = (dp[i]+minus_dp[i])%div

    print(dp[n])