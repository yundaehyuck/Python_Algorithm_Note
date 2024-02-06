from sys import stdin

#n번째 페리 수열의 길이
#= n-1번째 페리 수열의 길이 + n보다 작으면서 n과 서로소인 정수의 개수
#= n-1번째 페리 수열의 길이 + phi(n)

def phi(n):
    
    result = n

    p = 2

    while p*p <= n:
        
        if n % p == 0:
            
            while n % p == 0:
                
                n = n//p
            
            result -= result//p
        
        p += 1
    
    if n > 1:
        
        result -= result//n
    
    return result

dp = [0]*(10001)

dp[1] = 2

for i in range(2,10001):
    
    dp[i] = dp[i-1] + phi(i)

p = int(stdin.readline())

for _ in range(p):
    
    k,n = map(int,stdin.readline().split())

    print(k,dp[n])