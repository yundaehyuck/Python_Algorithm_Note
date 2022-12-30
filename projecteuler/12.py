triangle = [0]*(100000)

i = 1
n = 1

while 1:
    
    triangle[i] = triangle[i-1] + n

    num = triangle[i]

    p = 2

    divisor = 1

    while p*p <= num:
        
        count = 0
        
        if num % p == 0:
            
            while num % p == 0:
                
                num //= p

                count += 1
            
            divisor *= count+1
        
        p = p + 1
    
    if num > 1:
        
        divisor *= 2
    
    if divisor >= 500:
        
        break
    
    else:
        
        i += 1
        n += 1

print(triangle[i])