from sys import stdin

#dp[j][i] = 서로 다른 1부터 i까지 사용해서 j를 만드는 방법의 수

mod = 100999

dp = [[0]*2001 for _ in range(2001)]

#초기화
for i in range(2001):
    
    dp[0][i] = 1

#구성이 같은데, 순서가 다르면 같다고 취급
for i in range(1,2001): #도구
    
    for j in range(1,2001): #목적
        
        if i <= j:
            
            #1부터 i-1만을 사용해서 j-i를 만드는 방법의 수에 i만 더해주고
            #1부터 i-1만을 사용해서 j를 만드는 방법의 수에는 이미 j니까
            #그것도 1부터 i까지 사용해서 만드는 방법의 수이며
            #굳이 i를 안더해줘도 되는
            dp[j][i] = dp[j-i][i-1] + dp[j][i-1]
        
        else:
            
            #i > j이면, i를 안쓰고 j를 만들 수 있으므로..
            #1부터 i-1까지 사용해서 j를 만드는 방법의 수와 같다
            dp[j][i] = dp[j][i-1]
        
        dp[j][i] %= mod

T = int(stdin.readline())

answer = 0

for _ in range(T):
    
    n = int(stdin.readline())

    print(dp[n][n])

"""
#using euler's theorem
#"서로 다른 자연수만을 사용해서 자연수 n을 나타내는 방법의 수(patition with distinct parts)는 
#홀수만을 중복해서 사용해서 자연수 n을 나타내는 방법의 수(partition with odd parts)와 같다"

from sys import stdin

mod = 100999

dp = [0]*2001

dp[0] = 1

odd = list(range(1,2001,2)) #도구 : 홀수

for i in odd: #도구 먼저 

    for j in range(1,2001): #목적
        
        if j - i >= 0:

            dp[j] += dp[j-i] #j-i를 만드는 방법의 수 각각에 i를 더해주기만 하면 j를 만드는 방법의 수와 같다
            dp[j] %= mod

T = int(stdin.readline())

for _ in range(T):
    
    n = int(stdin.readline())

    print(dp[n])
"""