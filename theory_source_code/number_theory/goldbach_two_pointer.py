#find sum of four prime numbers is n

from sys import stdin

def is_prime(n):
    
    if n == 1:
        
        return False
    
    else:
        
        for i in range(2,int(n**(1/2))+1):
            
            if n % i == 0:
                
                return False
        
        return True

def goldbach(m):
    
    k = m//2

    for i in range(k):
        
        if is_prime(k-i) and is_prime(k+i):
            
            return [k-i,k+i]

n = int(stdin.readline())

if n < 8:
    
    print(-1)

else:
    
    if n % 2 == 0:
        
        n -= 4

        answer = goldbach(n)

        answer.append(2)
        answer.append(2)

    
    else:
        
        n -= 5

        answer = goldbach(n)

        answer.append(2)
        answer.append(3)
    
    print(*answer)