#i번째를 선택하면 인접한 원소 i-1, i+1번째 원소는 선택할 수 없을때, 선택된 원소들의 최대 합
n = int(input())

A = list(map(int,input().split()))

dp = [0]*(n+1)
dp[0] = A[0]

if n > 1:
    
    dp[1] = max(A[0],A[1])

#dp[i] = i번째 원소까지 봤을때, 선택된 원소들의 최대합
#i번째 원소를 선택한다면 i-1번째는 선택할 수 없으므로 dp[i] = dp[i-2] + A[i]
#i번째 원소를 선택할 수 없다면 dp[i] = dp[i-1]
for i in range(2,n):
    
    dp[i] = max(dp[i-1], dp[i-2] + A[i])

print(dp[n-1])