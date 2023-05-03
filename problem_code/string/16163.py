from sys import stdin

s = stdin.readline().rstrip()

s = "#"+"#".join(s)+"#"

n = len(s)

A = [0]*n

r = -1
p = -1

answer = 0

for i in range(n):
    
    if r < i:
        
        A[i] = 0
    
    else:
        
        ii = 2*p-i
        A[i] = min(r-i,A[ii])
    
    while i-A[i]-1 >= 0 and i+A[i]+1 < n and s[i-A[i]-1] == s[i+A[i]+1]:
        
        A[i] += 1
    
    if A[i] % 2 == 0:
        
        answer += (A[i]//2)
    
    else:
        
        answer += (A[i]//2+1)
    
    if i+A[i] > r:
        
        r = i+A[i]
        p = i


print(answer)