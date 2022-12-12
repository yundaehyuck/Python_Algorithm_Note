def power(a:float, n:int):
    
    result = 1
    
    while n:
        
        if n % 2 == 1:
            
            result *= a
        
        a *= a
        
        n = n//2
    
    return result