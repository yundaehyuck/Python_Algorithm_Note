from sys import stdin

n = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

k = int(stdin.readline())

i = 0
j = 0

summation = A[0]

answer = 0

while 1:
    
    if summation > k:
        
        answer += (n-j)

        i += 1
        summation -= A[i-1]
    
    else:
        
        j += 1

        if j == n:
                 
            break
           
        summation += A[j]
    
print(answer)