from sys import stdin

def pisano(m):
    
    a0,a1 = 0,1
    
    period = 1
    
    for i in range(m*m):

        a0,a1 = a1,(a0+a1)%m
        
        if (a0 == 0 and a1 == 1):

            return period

        else:

            period += 1

mod = 1000000

period = pisano(mod)

n = int(stdin.readline())

n = n % period

dp = [0]*(n+1)

dp[1] = 1

for i in range(2,n+1):
    
    dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[n])