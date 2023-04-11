from sys import stdin

n = int(stdin.readline())

i = 1
j = 1

summation = 1

answer = 0

while i != n+1 and j != n+1:
    
    if summation < n:
        
        j += 1

        if j == n+1:
            
            break

        summation += j
    
    elif summation == n:

        answer += 1
        i += 1
        j += 1
        summation -= i-1

        if j == n+1:
            
            break

        summation += j
    
    else:
        
        i += 1
        summation -= i-1
    

print(answer)