#원소를 최소로 바꿔서 임의의 두 수가 약수-배수가 되도록 만들기

n = int(input())

A = list(map(int,input().split()))

#배열을 정렬하고
A.sort()

#dp[i] = i번째까지 봤을 때 가장 긴 증가하는 약수 부분 수열의 길이
dp = [1]*n

#i = 1,2,...,n-1에 대하여 j = 0,1,2,..,i-1에 대해 A[i]가 A[j]로 나누어 떨어지면, dp[i] = dp[j] + 1
for i in range(1,n):
    
    for j in range(i):
        
        if A[i] % A[j] == 0:
            
            dp[i] = max(dp[i], dp[j] + 1)
            
print(n - max(dp))