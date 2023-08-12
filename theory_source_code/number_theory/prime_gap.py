#prime gap

from sys import stdin

def is_prime(n):
    
    if n == 1:
        
        return False
    
    else:
        
        for i in range(2,int((n+1)**(1/2))+1):
            
            if n % i == 0:
                
                return False
        
        return True

#연속하는 두 소수의 차이는 10^9내에서 최대 282이다.

T = int(stdin.readline())

for i in range(1,T+1):
    
    z = int(stdin.readline())

    z_root = int(z**(1/2))

    for j in range(z_root,-1,-1):
        
        if is_prime(j) == True:
            
            p1 = j
            break
    
    for j in range(p1+1,10**9+283):
        
        if is_prime(j) == True:
            
            p2 = j
            break
    
    for j in range(p1-1,-1,-1):
        
        if is_prime(j) == True:
            
            p3 = j
            break
    
    r1 = p1*p2
    r2 = p1*p3

    if r1 <= z:

        print(f"Case #{i}: {r1}")
    
    else:
        
        print(f"Case #{i}: {r2}")