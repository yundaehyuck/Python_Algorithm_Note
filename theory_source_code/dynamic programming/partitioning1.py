from sys import stdin

#연속한 구간의 오렌지를 상자에 포장할때, 포장 비용이 k + (구간 내 오렌지 개수) * (오렌지 크기 최대 - 최소)
#모든 오렌지를 여러개의 상자에 포장할때 비용의 최솟값 
n,m,k = map(int,stdin.readline().split())

A = []

for _ in range(n):
    
    a = int(stdin.readline())
    A.append(a)

#dp[i] = i번째 오렌지까지 봤을때 포장한 비용의 최솟값
INF = 10**18
dp = [INF]*n
dp[0] = k #0번 오렌지 포장하면, 최대 = 최소이므로 포장 비용은 k

#i  =1,2,3...,n-1에 대하여....
for i in range(1,n):
    
    #j ~ i번 구간의 오렌지를 상자에 담는다
    #j = i,i-1,..,i-m+1로 최대 m개 담을 수 있으므로
    #역순으로 순회해야 j ~ i 구간의 최대 최소를 o(n)으로 빠르게 구할 수 있다
    #정방향으로 순회하면 o(n^2)이 된다
    Max = 0
    Min = INF

    for j in range(i,max(0,i-m+1)-1,-1):
        
        if Max < A[j]:
            
            Max = A[j]
        
        if Min > A[j]:
            
            Min = A[j]
        
        cost = k + (i - j + 1)*(Max-Min)

        #j ~ i번 오렌지를 상자에 담으면, 지금까지 비용은 dp[j-1]이므로 dp[i] = max(dp[j-1]+cost,dp[i])
        if j >= 1 and dp[j-1] + cost < dp[i]:
            
            dp[i] = dp[j-1] + cost
        
        #j = 0인 경우는 0 ~ i번 오렌지를 상자에 담으므로, 지금까지 비용이 없으니 dp[i] = max(dp[i],cost)
        elif j == 0 and cost < dp[i]:
            
            dp[i] = cost

print(dp[n-1])