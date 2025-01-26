#길이가 정확히 d인 수도관의 용량들 중 최댓값
#수도관의 용량 = 구성된 수도관들의 용량들 중 최솟값
from sys import stdin

d,p = map(int,stdin.readline().split())

INF = 10**18
dp = [-1]*(d+1)
dp[0] = INF

A = []

for _ in range(p):
    
    l,c = map(int,stdin.readline().split())
    A.append((l,c))

#dp[i] = 길이가 i인 수도관의 가능한 용량들 중 최댓값
# = 길이의 합이 i인 수도관의 용량들 중 최솟값의 최댓값
#dp[i] = max(dp[i], min(dp[i-l],c))
#여기서 dp[i-l] != -1이어야, 즉 길이가 i-l인 수도관이 존재해야함
#dp = [-1]*(d+1)로 하는 이유는? max(dp[i], min(dp[i-l],c))가 계산되어야하니까
for l,c in A:
    
    for i in range(d,l-1,-1):
        
        if dp[i-l] != -1:

            dp[i] = max(dp[i], min(dp[i-l], c))

print(dp[d])