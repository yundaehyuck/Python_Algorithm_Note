#최소 길이 사이클
# 플로이드 워셜을 사용
# dp[i][i] = i번에서 시작해서 i번으로 오는 최단 거리

from sys import stdin

v,e = map(int,stdin.readline().split())

INF = 10**18

dp = [[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    
    a,b,c = map(int,stdin.readline().split())
    dp[a][b] = c

for k in range(1,v+1):
    
    for i in range(1,v+1):
        
        for j in range(1,v+1):
            
            dp[i][j] = min(dp[i][j],dp[i][k] + dp[k][j])

answer = INF

for i in range(1,v+1):
    
    if answer > dp[i][i]:
        
        answer = dp[i][i]

if answer == INF:
    
    print(-1)

else:
    
    print(answer)