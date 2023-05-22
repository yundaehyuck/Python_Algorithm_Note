def is_perfect(n):
    
    if int((n**(1/2)))**2 == n:
        
        return True
    
    return False

def is_fib(n):
    
    x = 5*n*n+4
    y = 5*n*n-4
    
    if is_perfect(x) or is_perfect(y):
        
        return True
    
    return False