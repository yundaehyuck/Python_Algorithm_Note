from sys import stdin

N = 2**15

#dp[i][j] = i를 j개의 제곱수 합으로 나타낼 수 있는 경우의 수
dp = [[0]*5 for _ in range(N+1)]

m = int(N**(1/2))

for i in range(1,m+1):
    
    #초기화    
    dp[i*i][1] = 1 #i*i는 i 1개로 나타낼 수 있다

    for j in range(i*i,N+1):
        
        for k in range(2,5):
            
            #j는 j-(i*i) + (i*i)로 나타낼 수 있다
            #따라서, j-(i*i)를 나타낼 수 있는 경우의 수들 각각에 (i*i)만 더해주면 j가 되므로..
            #k-1개의 제곱수로 j-(i*i)를 나타낼 수 있는 경우의 수들 각각에 1개의 제곱수 i*i만 더해준다
            #따라서, j를 k개의 제곱수 합으로 나타낼 수 있는 경우의 수는, k-1개의 제곱수로 j-(i*i)를 나타낼 수 있는 경우의 수와 같다.
            dp[j][k] = dp[j][k] + dp[j-i*i][k-1]

while 1:
    
    n = int(stdin.readline())

    answer = 0
    
    if n == 0:
        
        break
    
    else:
        
        for i in range(1,5):
            
            answer += dp[n][i]
        
        print(answer)