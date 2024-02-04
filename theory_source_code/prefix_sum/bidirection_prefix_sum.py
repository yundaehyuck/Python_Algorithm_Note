n = int(input())

A = list(map(int,input().split()))

#si = i명이 거짓말한다고 했을때, 거짓말하는 사람의 수

s1 = [0]*(n+1) #우측으로 누적
s2 = [0]*(n+1) #좌측으로 누적

#A[i] = k, k명 이상이 거짓말하고 있다
#거짓말하는 사람이 k-1,k-2,k-3,..일때 거짓말하는 사람
#A[i] = -k, k명 이하가 거짓말하고 있다
#거짓말하는 사람이 k+1,k+2,.k+3,..일때 거짓말하는 사람
for i in range(n):
    
    if A[i] > 0 and A[i] <= n:
        
        s2[A[i]-1] += 1
    
    elif A[i] <= 0 and A[i] > -n:
        
        s1[-A[i]+1] += 1

#k+1에 표시한 경우, 0에서 n-1방향으로 누적합해주면
#k+1,k+2,k+3,..,n에 모두 +1을 해준 효과
for i in range(1,n+1):
    
    s1[i] += s1[i-1] 

#k-1에 표시한 경우, n-1에서 0방향으로 누적합해주면
#k-1,k-2,...,0에 모두 +1을 해준 효과
for i in range(n-1,-1,-1):
    
    s2[i] += s2[i+1]

count = 0
answer = []

#i명이 거짓말한다고 할때, 실제 거짓말하는 사람 수 s1[i]+s2[i]가 i인 경우만 정답
for i in range(n+1):
    
    if (s1[i]+s2[i]) == i:
        
        answer.append(i)
        count += 1        

print(count)
print(*answer)