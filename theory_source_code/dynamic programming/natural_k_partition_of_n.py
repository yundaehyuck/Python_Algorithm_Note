#정수 n을 k개의 자연수로 분할하는 방법의 수

#dp[i][j] = i를 j개의 자연수로 분할하는 방법의 수
#dp[0][0] = 1

#최솟값이 1인 분할 : 나머지 j-1개에 i-1을 분배하면 되므로 dp[i-1][j-1]
#최솟값이 2 이상인 분할: 전체 항에 1씩 분배하면 i-j를 사용할 수 있고 이를 j개의 항에 분배하면 됨 dp[i-j][j]
#dp[i][j] = dp[i-j][j] + dp[i-1][j-1]

n = int(input())
k = int(input())

dp = [[0]*(k+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(1,n+1):
    
    for j in range(1,min(i,k)+1):
        
        if i == j:
            
            dp[i][j] = 1
        
        else:
            
            dp[i][j] = dp[i-j][j] + dp[i-1][j-1]
    
print(dp[n][k])