#왼쪽 끝, 오른쪽 끝중 하나를 선택하고 k번째 선택한 경우 A[i]*k 이익을 얻을 때
#모든 벼를 수확한 경우 얻는 최대 이익
n = int(input())

A = []

for _ in range(n):
    
    m = int(input())
    A.append(m)

#dp[i][j]:[i,j]에 있는 벼들로 얻을 수 있는 최대이익
dp = [[0]*n for _ in range(n)]

#벼가 i번째 벼 하나만 남은 경우
#n번째 수확해야하므로 A[i]*n
for i in range(n):
    
    dp[i][i] = A[i]*n

#[i,j]에서 0~i-1, j+1~n-1 벼는 선택했으므로, n-1-j+i+1번째 벼를 선택하게 됨
# i번째 벼를 선택하면 A[i]*(n-j+i), [i+1,j] 구간이 남으므로, 여기서 얻는 이익 dp[i+1][j]
#j번째 벼를 선택하면 A[j]*(n-j+i), [i,j-1] 구간이 남으므로, 여기서 얻는 이익 dp[i][j-1]
for i in range(n-1,-1,-1):
    
    for j in range(i,n):
        
        k = i + n-1-j + 1

        if i+1 <= n-1 and j-1 >= 0:

            dp[i][j] = max(dp[i][j],dp[i][j-1] + A[j]*k,dp[i+1][j] + A[i]*k)
        
        elif i+1 <= n-1:
            
            dp[i][j] = max(dp[i][j],dp[i+1][j] + A[i]*k)
        
        elif j-1 >= 0:
            
            dp[i][j] = max(dp[i][j-1],dp[i][j-1] + A[j]*k)
            
print(dp[0][n-1])