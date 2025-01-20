#달리면 지침지수 1 증가, 쉬면 1 감소
#지침지수가 m이면 달릴수 없다
#한번 쉬면 지침지수가 0이 될때까지 쉰다
#마지막에 지침지수는 0이어야한다
from sys import stdin

n,m = map(int,stdin.readline().split())

A = []

for _ in range(n):
    
    d = int(stdin.readline())
    A.append(d)

D = [0,A[0]]

for i in range(1,n):
    
    D.append(D[-1] + A[i])

#dp[i] = i번쨰 시간에 달릴 수 있는 최대거리
dp = [0]*(n+1)

for i in range(1,n+1):
    
    dp[i] = max(dp[i], dp[i-1]) #쉬는 경우

    for j in range(1,m+1):
        
        #i번째 시간부터 j시간동안 달리고, j시간동안 쉬었을때
        if i+2*j-1 <= n:

            dp[i+2*j-1] = max(dp[i+2*j-1], dp[i-1] + (D[i+j-1] - D[i-1])) 

print(dp[n])

"""
n,m = map(int,input().split())

D = []

for _ in range(n):
    
    d = int(input())
    D.append(d)

#dp[i][j] = i번째에 지침지수가 j
dp = [[0]*(m+1) for _ in range(n)]

dp[0][1] = D[0]

for i in range(1,n):
    
    #달리는 경우
    for j in range(m):
    
        dp[i][j+1] = max(dp[i][j+1],dp[i-1][j] + D[i])
    
    #쉬는거 초기화
    dp[i][0] = dp[i-1][0]

    #i-j분에 j 지침지수가 있는데 j분 쉬면 i분에 지침지수가 0이 되는
    for j in range(1,m+1):    
      
        if i-j >= 0:
            
            dp[i][0] = max(dp[i][0],dp[i-j][j])

print(dp[n-1][0])

"""

"""
n,m = map(int,input().split())

D = []

for _ in range(n):
    
    d = int(input())
    D.append(d)

#dp[i][j][k] = i번째에 지침지수가 j이고 쉬면 k = 0, 달리면 k = 1
dp = [[[0,0] for _ in range(m+1)] for _ in range(n)]

dp[0][1][1] = D[0]
dp[0][0][0] = 0

for i in range(1,n):

    #처음에 달려서 지침지수가 1이 되는 경우는
    #처음에 쉬고 지침지수가 0인 경우에서 달려야
    dp[i][1][1] = max(dp[i][1][1],dp[i-1][0][0] + D[i])

    for j in range(m):
        
        if j >= 1:

            dp[i][j+1][1] = max(dp[i][j+1][1],dp[i-1][j][1] + D[i])
        
        #달리다가 쉬는 경우, 쉬는 중에 쉬는 경우
        dp[i][j][0] = dp[i-1][j][0] #쉬는 경우 초기화
        dp[i][j][0] = max(dp[i][j][0],dp[i-1][j+1][1], dp[i-1][j+1][0])

print(dp[n-1][0][0])
"""