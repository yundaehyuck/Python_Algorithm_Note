from sys import stdin

n = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

dp = [0]*n

min_A = A[0]

for i in range(1,n):
    
    x = A[i] - min_A

    if x > dp[i-1]:
        
        dp[i] = x
    
    else:
        
        dp[i] = dp[i-1]

        if min_A > A[i]:
            
            min_A = A[i]
    
print(*dp)