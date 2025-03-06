#연속하는 구간의 상태를 1번 바꿀때 켜져있는 원소 합의 최댓값
n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

#초기 합을 s라 하고,
#켜져있으면 D[i] = -A[i], 꺼져있으면 D[i] = A[i]라 하면면
s = 0

D = []

for i in range(n):
    
    if B[i] == 1:
        
        s += A[i]
        D.append(-A[i])
    
    else:
        
        D.append(A[i])

#정답은 s + maxsum(D[i,j])
#즉, D배열에서 연속하는 구간의 최대 원소 합을 구하면 된다
INF = 10**18

dp = [-INF]*n

dp[0] = D[0]

for i in range(1,n):
    
    dp[i] = max(dp[i-1] + D[i], D[i])

print(s + max(dp))