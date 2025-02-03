#배열의 원소를 여러개의 구간으로 나눈다
#각 구간은 인접하지 않아야하고, 겹치지 않아야한다
#각 원소는 구간에 포함되지 않아도 된다
#1개 이상의 연속된 원소를 포함해야한다
#정확히 m개의 구간을 사용해야한다
n,m = map(int,input().split())

A = []

for _ in range(n):
    
    a = int(input())
    A.append(a)

#dp[i][j] = i번째까지 썼을때 j번째 조까지 총 합의 최댓값
dp = [[-3276811]*(m+1) for _ in range(n)]
dp[0][1] = A[0] #0번 원소를 쓰면, 구간은 1개이므로 

#i = 1,2,..,n-1에 대하여..
for i in range(1,n):
    
    #j = 1,2,..,m번째 구간에 대해
    for j in range(1,m+1):

        max_s = -3276811
        s = 0 #k ~ i번째 구간의 원소합

        dp[i][j] = dp[i-1][j] #i번째 원소를 쓰지 않는 경우

        #j번째 조에 k번째부터 i번째까지 쓸때
        for k in range(i,-1,-1):

            s += A[k]

            if max_s < s:
                
                max_s = s

            if j == 1: #j = 1인 경우 구간은 1개밖에 없으므로... dp[i][j] = max_s
                
                dp[i][j] = max(dp[i][j], max_s)

            else: #j >= 2인 경우 구간이 2개 이상 있으므로
                
                #구간이 인접하지 않아야하므로
                #0 ~ k-2번째원소를 j-1개 구간에 담고, k-1번째 건너뛰고 k ~ i번째 원소를 j번째 구간에 담고
                #dp[i][j] = max(dp[i][j], dp[k-2][j-1] + max_s)
                if k >= 2: 

                    dp[i][j] = max(dp[i][j], dp[k-2][j-1] + max_s)    

print(dp[n-1][m])