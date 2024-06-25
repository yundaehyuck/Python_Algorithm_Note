#i < j < k < l인 (i,j,k,l)에 대하여 A[j] - A[i] + A[l] - A[k]의 최댓값을 구하는 문제
n = int(input())

A = list(map(int,input().split()))

#A는 양수인데, A[j] - A[i]는 A[j] = 0, A[i] = 10000..이라 음수가 가능
INF = 10000000

dp1 = [-INF]*(n+1)
dp2 = [-INF]*(n+1)

#A[j] - A[i]의 최댓값 + A[l] - A[k]의 최댓값으로 나눠서 문제를 해결

min_value = A[0]

#dp1[j] = i < j, i = 0,1,2,..,j-1인 모든 (i,j)에 대하여 A[j] - A[i]의 최댓값
#j = 0,1,2,...,n-1일때 각각 A[i]의 최솟값에 대해 A[j] - (min_value)
#j가 커지면서 A[i]의 최솟값을 갱신
#dp1[j] = max(dp1[j-1], A[j] - min_value)하면 0~j 구간의 모든 (i,j)에 대해 최댓값
for j in range(1,n):
    
    if dp1[j-1] > A[j] - min_value:
        
        dp1[j] = dp1[j-1]
    
    else:
        
        dp1[j] = A[j] - min_value
    
    if A[j] < min_value:
        
        min_value = A[j]

#dp2[k] = k < l, l = k+1,k+2,...,n-1인 모든 (k,l)에 대해 A[l] - A[k]의 최댓값
#k = n-1,n-2,n-3,...,0에 대하여 (A의 최댓값) - A[k]
#k가 작아지면서 A[k]의 최댓값을 갱신
#dp2[k] = max(dp2[k+1], max_value - A[k])하면 k~n-1 구간의 모든 (k,l)에 대해 최댓값
max_value = A[n-1]

for k in range(n-2,-1,-1):
    
    if dp2[k+1] > max_value - A[k]:
        
        dp2[k] = dp2[k+1]
    
    else:
        
        dp2[k] = max_value - A[k]
    
    if A[k] > max_value:
        
        max_value = A[k]

answer = -INF

#dp1은 0~j구간 dp2는 k~n-1구간을 커버하므로
#dp1[i]+dp2[i+1]은 모든 i < j < k < l인 (i,j,k,l)에 대해 A[j]-A[i] + A[l]-A[k]의 최댓값이 된다
for i in range(n-1):
    
    if dp1[i] + dp2[i+1] > answer:
        
        answer = dp1[i]+dp2[i+1]

print(answer)