#n개의 행렬을 곱했을때 가능한 연산량의 최솟값

from sys import stdin

n = int(stdin.readline())

A = []

for _ in range(n):
    
    r,c = map(int,stdin.readline().split())
    A.append((r,c))

INF = 10**23
dp = [[0]*n for _ in range(n)] #dp[i][j] = i~j번 행렬끼리의 곱의 연산량 최솟값

#구간의 길이
#길이가 1인 경우는 곱하지 않으므로 0
for length in range(2,n+1):
    
    #구간의 시작점
    for i in range(n-length+1):
        
        j = i + length - 1 #이러면 i ~ j까지는 길이가 length

        dp[i][j] = INF #초기값
        
        #i~j번까지 행렬을 곱하는 방법은?
        #i ~ k번까지 행렬을 곱하고, k+1~j번까지 행렬을 곱한 다음, 두 행렬을 곱한다

        #i~k까지 곱 dp[i][k], 크기:(A[i][0]*A[k][1])
        #k+1 ~ j까지 곱 dp[k+1][j], 크기:(A[k][1]*A[j][1])
        #두 행렬을 곱하면 A[i][0]*A[k][1]*A[j][1] 필요
        for k in range(i,j):
            
            dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + A[i][0]*A[k][1]*A[j][1])

print(dp[0][n-1])