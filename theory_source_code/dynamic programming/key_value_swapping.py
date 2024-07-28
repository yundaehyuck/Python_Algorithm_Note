#단맛이 a, 짠맛이 b인 n개의 음식을 먹을때
#단맛의 합이 x를 넘지 않거나 y를 넘지 않도록 최대로 먹을 수 있는 개수

"""
n,x,y = map(int,input().split())

f = []

for _ in range(n):
    
    a,b = map(int,input().split())

    f.append((a,b))

#전형적인 배낭 문제
#dp[i][j][k] = i번째 음식까지 단맛의 합이 j, 짠맛의 합이 k가 되도록 먹은 최대 음식의 개수(O(NXY), 8*10^9로 시간초과)

#dp[i][j][k] = i번째 음식까지 단맛의 합이 k가 되도록 j개를 선택할때 짠맛의 최솟값(O(N^2X) 64*10^6으로 가능)

INF = 10**6

dp = [[[INF]*(x+1) for _ in range(n+1)] for _ in range(n)]

a,b = f[0]

dp[0][0][0] = 0

if a <= x:

    dp[0][1][a] = b

for i in range(1,n):
    
    a,b = f[i]

    for j in range(n+1):
        
        for k in range(x,-1,-1):
            
            dp[i][j][k] = min(dp[i-1][j][k], dp[i][j][k]) #i번째 음식을 먹지 않아도 먹은게 j개이고 단맛 합이 k가 되는 경우가 있다

            if j >= 1 and k-a >= 0:

                dp[i][j][k] = min(dp[i-1][j-1][k-a] + b, dp[i][j][k])


#n번째까지 음식 먹었을 때 dp[n-1]
#먹은 음식의 수가 i개이고 단맛의 합이 j인 경우 dp[n-1][i][j]
#이 짠맛의 합의 최솟값이 y이하가 되는 i의 최댓값을 찾으면

#i+1이면 단맛의 합이 x를 넘거나 짠맛의 합이 y를 넘게 된다
answer = 0

for i in range(n-1,0,-1):
    
    for j in range(x+1):
        
        if dp[n-1][i][j] <= y: 
            
            answer = i
            break
    
    if answer != 0:
        
        break

print(answer+1)
"""

#배낭 문제니까 dp[i][j][k]에서 i부분을 지워서 2차원 배열로 만들 수 있을 것 같다
n,x,y = map(int,input().split())

f = []

for _ in range(n):
    
    a,b = map(int,input().split())

    f.append((a,b))

#dp[j][k] = 단맛의 합이 k가 되도록 j개를 선택할때 짠맛의 최솟값

INF = 10**6

dp = [[INF]*(x+1) for _ in range(n+1)]

a,b = f[0]

dp[0][0] = 0

if a <= x:

    dp[1][a] = b

#O(N^2X)긴 한데 3차원 배열로 구할때보다 시간도 훨씬 빠르고 메모리도 덜 든다
for i in range(1,n):
    
    a,b = f[i]
    
    for j in range(n,-1,-1):
        
        for k in range(x,-1,-1):
            
            if j >= 1 and k-a >= 0:

                dp[j][k] = min(dp[j-1][k-a] + b, dp[j][k])

answer = 0

for i in range(n-1,0,-1):
    
    for j in range(x+1):
        
        if dp[i][j] <= y:
            
            answer = i
            break
    
    if answer != 0:
        
        break

print(answer+1)