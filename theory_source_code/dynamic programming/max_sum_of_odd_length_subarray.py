#모든 홀수 길이 부분 배열중 원소 합이 가장 큰 경우 찾기

from sys import stdin

z = int(stdin.readline())

for _ in range(z):

    n = int(stdin.readline())

    A = list(map(int,stdin.readline().split()))

    INF = 100000000000000000000000000

    #dp[i][0] = i번째 원소까지 봤을때, 홀수 길이인 연속하는 부분 배열의 합중 최댓값
    #dp[i][1] = i번째 원소까지 봤을때, 짝수 길이인 연속하는 부분 배열의 합중 최댓값
    #원소 합이 음수일 수 있으니.. 초기화를 음의 무한대로
    dp = [[-INF]*2 for _ in range(n)]

    dp[0][0] = A[0] #원소 하나는 홀수 길이

    #짝수 길이 + 원소 = 홀수 길이, dp[i][0] = max(dp[i-1][1] + A[i], A[i])
    #홀수 길이 + 원소  = 짝수 길이, dp[i][1] = dp[i-1][0] + A[i]
    #원소 하나는 홀수 길이이므로 dp[i][1]에 들어가지 않아
    for i in range(1,n):

        dp[i][0] = max(A[i], dp[i-1][1] + A[i])
        dp[i][1] = dp[i-1][0] + A[i]
    
    #중간에 최대 합이 나올수도 있기 때문에 정답은 max(dp[i][0])
    answer = -INF

    for i in range(n):
        
        if answer < dp[i][0]:
            
            answer = dp[i][0]
    
    print(answer)