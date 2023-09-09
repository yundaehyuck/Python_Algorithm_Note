import math

n = int(input())

A = list(map(int,input().split()))

A.sort()

m = (n+1)//2-1

answer = 0

for i in range(m+1):
    
    answer += int(math.log2(A[i]))

print(answer+1)