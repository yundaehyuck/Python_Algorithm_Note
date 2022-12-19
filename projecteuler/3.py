n = 600851475143

p = 2

while p*p <= n:
    
    if n % p == 0:
        
        while n % p == 0:
            
            n = n//p
    
    p = p + 1

if n > 1:
    
    if n <= p:
        
        print(p)
    
    else:
        print(n)