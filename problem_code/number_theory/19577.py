def phi(n):
    
    result = n

    p = 2

    while p*p <= n:
        
        if n % p == 0:
            
            while n % p == 0:
                
                n = n//p
            
            result -= result//p
        
        p += 1
    
    if n > 1:
        
        result -= result//n
    
    return result

n = int(input())

answer = n

for i in range(2,int((n**(1/2)))+1):
    
    if n % i == 0:
        
        x = n//i

        if phi(i) == x:
            
            if answer > i:
                
                answer = i
        
        elif phi(x) == i:
            
            if answer > x:
                
                answer = x

if answer != n:
    
    print(answer)

elif n == 1 or n == 2:
    
    print(n)

else:
    
    print(-1)