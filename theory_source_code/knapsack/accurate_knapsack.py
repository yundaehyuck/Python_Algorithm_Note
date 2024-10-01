#정확히 배낭 크기만큼 배낭에 담을 수 있고, 원하는 양보다 더 많이 담지 않을때 원하는 양을 만드는 방법의 수

"""
n,m = map(int,input().split())

A = list(map(int,input().split()))

INF = 10**12

#dp[i] = i개 그릇 만드는데 해야하는 최소 요리 횟수
dp = [INF]*(n+1)
dp[0] = 0

for i in range(1,n+1):
    
    for j in range(m): #j = 0,1,..번째 도구를 사용할때,
        
        for k in range(j,m): #동시에 k = j,j+1,...번째 도구도 사용할 수 있다면,
            
            if j == k: #한손으로 요리하는 경우
                
                v = A[j]
            
            else: #양손으로 요리하는 경우
                
                v = A[j] + A[k] #정확히 해당 크기만큼 담고

            if i >= v: #목표로 하는 양 i보다 많이 담지 말아야하므로

                dp[i] = min(dp[i], dp[i - v] + 1)

if dp[n] == INF:
    
    print(-1)

else:
    
    print(dp[n])
"""

n,m = map(int,input().split())

A = list(map(int,input().split()))

#처음에 요리 가능한 그릇의 수를 모두 만들어두고
S = []

for i in range(m):
    
    S.append(A[i]) #한손으로 요리하는
    
    for j in range(i+1,m):
        
        S.append(A[i] + A[j]) #양손으로 요리하는

INF = 10**12

#dp[i] = i개 그릇 만드는데 해야하는 최소 요리 횟수
dp = [INF]*(n+1)
dp[0] = 0 #0그릇 만드는데 당연히 0번

#i = 1,2,3...,n에 대하여
for i in range(1,n+1):
    
    #가능한 만드는 요리 횟수...
    for j in range(len(S)):
        
        v = S[j]
        
        if i >= v: #i그릇을 만드는데 i그릇보다 더 많이 만들지는 않아야하므로

            dp[i] = min(dp[i], dp[i - v] + 1)

if dp[n] == INF:
    
    print(-1)

else:
    
    print(dp[n])