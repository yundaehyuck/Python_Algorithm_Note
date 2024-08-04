#주어진 배열에서 연속하는 부분 배열 중 가장 큰 원소 합
from sys import stdin

n = int(stdin.readline())

num_list = list(map(int,stdin.readline().split()))

#dp[i] = 0~i번째 원소까지 연속하는 부분 배열 중 가장 큰 원소 합
dp = [0] * n

dp[0] = num_list[0]

max_num = dp[0]

#이전까지 가장 큰 부분 배열합 + 현재 원소 와 현재 원소 중 더 큰 값으로 갱신해나감
#dp[i] = max(dp[i-1] + A[i], A[i])
for i in range(1,n):
    
    dp[i] = max(dp[i-1]+num_list[i],num_list[i])

    if dp[i] > max_num:
        
        max_num = dp[i]

print(max_num)