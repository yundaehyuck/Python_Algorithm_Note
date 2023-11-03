#3개 문자열 X,Y,Z의 LCS 구하기
X = input()
Y = input()
Z = input()

n = len(X)
m = len(Y)
l = len(Z)

#문자열 X[1,2,...,i]와 Y[1,2,..,j]와 Z[1,2,..,k]의 가장 긴 공통부분문자열의 길이 dp[i][j][k]
dp = [[[0]*(l+1) for _ in range(m+1)] for _ in range(n+1)]

#X[i], Y[j], Z[k]가 모두 같을때, dp[i][j][k]는 dp[i-1][j-1][k-1]에 1을 더해준것
#그렇지 않으면, 각각 하나 뺀 dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1]중 최댓값
for i in range(1,n+1):
    
    for j in range(1,m+1):
        
        for k in range(1,l+1):
            
            if X[i-1] == Y[j-1] and Y[j-1] == Z[k-1]:
                
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            
            else:
                
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

#모두 순회해서 dp배열을 채우면, dp[n][m][l]에 LCS의 길이가 있다
print(dp[n][m][l])