#길이가 k인 증가하는 부분 수열의 개수

from sys import stdin

while 1:

    n,k = map(int,stdin.readline().split())

    if n == 0 and k == 0:
        
        break

    A = list(map(int,stdin.readline().split()))

    #dp[i][x] = i번째 원소를 마지막으로 하는 길이가 x인 증가하는 부분 수열의 개수

    dp = [[0]*(k+1) for _ in range(n)]

    dp[0][1] = 1

    for i in range(1,n):
        
        dp[i][1] = 1 #dp[i][1] = 1, i번째 원소만 붙이면 되니까까

        #i 이전의 모든 j = 0,1,2,..,i-1에 대하여,
        for j in range(i):
            
            for x in range(1,min(j+2,k)):
                
                #A[i] > A[j]이면 A[i]를 A[j] 뒤에 붙일 수 있으므로,
                #dp[i][x+1] += dp[j][x]
                if A[i] > A[j]:
            
                    dp[i][x+1] += dp[j][x]
    
    #길이가 k인 증가하는 부분 수열의 개수는
    #i = 0,1,2,..에 대하여 dp[i][k]의 합
    count = 0
    
    for i in range(k-1,n):
        
        count += dp[i][k]
        
    print(count)