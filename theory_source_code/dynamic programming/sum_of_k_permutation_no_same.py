#1,2,3을 사용해 n을 만드는 방법의 수
#중복 사용 가능
#1+1+2와 1+2+1은 서로 다른 방법의 수

from sys import stdin

T = int(stdin.readline())

div = 1000000009

dp = [0]*1000001

dp[0] = 1
dp[1] = 1
dp[2] = 2

#n-1에 1을 더하면 n이므로 dp[n-1] 각각에 1을 붙여주면 된다
#n-2에 2를 더하면 n이므로 dp[n-2] 각각에 2를 붙여주면 된다
#n-3에 3을 더하면 n이므로 dp[n-3] 각각에 3을 붙여주면 된다
#dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

#나머지를 저장해둬야, 시간복잡도가 줄어든다.
for i in range(3,1000001):
    
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % div

for _ in range(T):
    
    n = int(stdin.readline())
    
    print(dp[n])