#greedy
from sys import stdin

a,k = map(int,stdin.readline().split())

answer = 0

while k != a:
    
    if k % 2 == 0:

        if k//2 < a:
            
            break
        
        k = k//2
    
    else:
        
        k -= 1
    
    answer += 1

print(answer + (k-a))

