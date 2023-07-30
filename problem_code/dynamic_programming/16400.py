from sys import stdin

def get_prime(n):
    
    result = [1]*(n+1)

    for i in range(2,int((n+1)**(1/2))+1):
        
        if result[i] == 1:
            
            for j in range(i*i,n+1,i):
                
                result[j] = 0
    
    return [i for i in range(2,n+1) if result[i] == 1]

n = int(stdin.readline())

prime_list = get_prime(n)

dp = [0]*(n+1)

dp[0] = 1

for p in prime_list:
    
    for i in range(2,n+1):
        
        if i-p >= 0:
            
            dp[i] += dp[i-p]
            dp[i] %= 123456789

print(dp[n] % 123456789)