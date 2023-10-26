#서로 다른 소수를 k개 사용해서 n을 만드는 방법의 수

from sys import stdin

def get_prime(n):
    
    result = [1]*(n+1)

    for i in range(2,int(((n+1)**(1/2)))+1):
        
        if result[i] == 1:
            
            for j in range(i*i,n+1,i):
                
                result[j] = 0
    
    return [i for i in range(2,n+1) if result[i] == 1]

prime = get_prime(1120)

dp = [[0]*15 for _ in range(1121)]

dp[0][0] = 1

#k개의 소수로 i를 만드는 방법의 수는..
#k-1개의 소수로 i-p를 만드는 방법의 수 각각에 p만 더해주면 된다
#구성이 같은데 순서가 달라도 같은 것으로 취급할려면, 도구 소수부터 순회해서..
for p in prime:
    
    #k를 역으로 순회해줘야 dp[24][3]에 2,11,11같이 중복해서 소수를 사용하는 경우를 방지한다
    for k in range(14,0,-1):
        
        for i in range(1,1121):

            if i >= p:

                dp[i][k] += dp[i-p][k-1]
            
T = int(stdin.readline())

for _ in range(T):
    
    n,k = map(int,stdin.readline().split())

    print(dp[n][k])