from sys import stdin

n = int(stdin.readline())

if n == 0:
    
    print(0)
    print(0)

elif n == 1:
    
    print(1)
    print(1)

elif n == -1:
    
    print(1)
    print(1)

else:
    
    dp = [0]*(abs(n)+1)
    dp[1] = 1

    for i in range(2,abs(n)+1):
        
        dp[i] = (dp[i-1]+dp[i-2])%1000000000
    
    if n > 1:

        print(1)
        print(dp[n])
    
    elif n < -1:
        
        if abs(n) % 2 == 0:
            
            print(-1)
            print(dp[abs(n)])
        
        else:
            
            print(1)
            print(dp[abs(n)])