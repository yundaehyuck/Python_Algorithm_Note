from sys import stdin

T = int(stdin.readline())

for _ in range(1,T+1):
    
    n = int(stdin.readline())

    if n == 1:
        
        print(1)
        continue

    answer = 0

    for d in range(9,1,-1):
        
        while n % d == 0:
            
            n //= d
            answer += 1
    
    if n >= 10:
        
        answer = -1
    
    print(answer)