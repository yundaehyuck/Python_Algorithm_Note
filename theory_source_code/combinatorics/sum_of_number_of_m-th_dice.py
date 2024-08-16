#1부터 m까지 쓰인 m면체 주사위 n개를 굴려서 나올 수 있는 숫자의 합의 경우의 수

n,m = map(int,input().split())

#dp[i][j] = i번째까지 봤을때 숫자의 합이 j인 경우의 수
dp = [[0]*(m*n+1) for _ in range(n)]

#0번까지 보면 가능한 숫자는 1부터 m까지 이므로 dp[0][i] = 1
for j in range(1,m+1):

    dp[0][j] = 1

#i = 1,2,3..,n번 자리에 대하여
#각 자리에는 j = 1,2,3,..,m까지 쓸 수 있고
#현재 눈의 합이 k이면... dp[i][k] += dp[i-1][k-j]
for i in range(1,n):

    for j in range(1,m+1):

        for k in range(m*n,-1,-1):

            if k >= j:

                dp[i][k] += dp[i-1][k-j]

print(dp[n-1])