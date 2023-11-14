from sys import stdin

#수열에서 일부 원소를 선택해서 최대공약수가 1이 되는 방법의 수
def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

mod = 10000003

n = int(stdin.readline())

s = []

for _ in range(n):
    
    a = int(stdin.readline())
    s.append(a)

#dp[i][j] = i번째 수까지 사용해서 최대공약수가 j가 되는 경우의 수
dp = [[0]*(100001) for _ in range(n)]

for i in range(n):
    
    dp[i][s[i]] = 1 #자기 자신만 사용하면 최대공약수는 자기 자신이 된다

for i in range(1,n):
    
    for j in range(1,100001):
        
        #i번째 수를 사용하지 않아도, 최대공약수가 j가 되는 경우의 수
        dp[i][j] += dp[i-1][j] 
        dp[i][j] %= mod
        
        g = gcd(s[i],j)
        
        #i번째 수를 사용해서 최대공약수가 g가 되는 경우의 수는...
        #s[i]와 j의 최대공약수가 g가 되는 모든 j에 대하여,
        #i-1번째 수까지 사용해서 최대공약수가 j가 되는 경우의 수에 i번째 수만 추가하면 된다
        
        dp[i][g] += dp[i-1][j] 
        dp[i][g] %= mod

print(dp[n-1][1])

"""
같은 수가 들어올 수 있다면...

처음에 초기화할때 dp[i][s[i]] += 1로 해야하는거 아니냐?

처음에 초기화할때는 해당 수 1개만 쓰는 방법의 수이고...

만약 s = [2,2,2,4]여서 dp[2][2]를 구한다고 한다면..?

처음에 초기화할때는 dp[2][2] = 1은 (2,2,2)에서 3번째 2만 쓴 (2)이고

나중에 2중 for문 돌때, dp[2][2] += dp[1][2]로 1번째 2만 쓴 (2)에서 2번째 2를 추가한 (2,2)가 더해진다.
"""