from sys import stdin

h,y = map(int,stdin.readline().split())

dp = [0]*(y+1)

dp[0] = h

for i in range(1,y+1):
    
    if i >= 5:

        dp[i] = max(int(dp[i-5]*1.35),int(dp[i-3]*1.2),int(dp[i-1]*1.05))
    
    elif i >= 3:
        
        dp[i] = max(int(dp[i-3]*1.2),int(dp[i-1]*1.05))
    
    else:
        
        dp[i] = int(dp[i-1]*1.05)

print(dp[y])