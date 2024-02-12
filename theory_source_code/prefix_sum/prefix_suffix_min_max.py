#배열에서 최대 M개를 지울때,
#A[2] - A[1] + A[3] - A[2] + ... + A[L] - A[L-1] = A[L] - A[1]의 최댓값
n,m = map(int,input().split())

A = list(map(int,input().split()))

#0~i 구간의 최솟값 prefix[i] = min(prefix[i-1],A[i])
prefix = [A[0]]

for i in range(1,n):
        
    prefix.append(min(prefix[-1],A[i]))


#i~n-1 구간의 최댓값 suffix[i] = max(suffix[i+1],A[i])
suffix = [0]*n

suffix[-1] = A[-1]

for i in range(n-2,-1,-1):
    
    suffix[i] = max(suffix[i+1],A[i])
    
answer = -1000000000000000000000000

for i in range(m+1):
    
    if answer < suffix[n-1-m+i] - prefix[i]:
        
        answer = suffix[n-1-m+i] - prefix[i]

print(answer)