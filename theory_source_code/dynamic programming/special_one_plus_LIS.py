#크기가 1씩 증가하는 가장 긴 증가하는 부분 수열의 길이

#[1,5,4,2,6,3,4]이면 [1,2,3,4]

n = int(input())

A = list(map(int,input().split()))

#dp[i] = 마지막 원소가 i인 부분 수열의 길이의 최댓값
dp = [0]*(10**6+1) #A 배열의 원소들의 최댓값이 10^6

#dp[A[i]] = dp[A[i]-1] + 1이면 된다
#A[i]-1이 존재하지 않으면 dp[A[i]] = 1로 자연스럽게 되고
dp[A[0]] = 1

for i in range(1,n):
    
    dp[A[i]] = dp[A[i]-1] + 1

print(max(dp))