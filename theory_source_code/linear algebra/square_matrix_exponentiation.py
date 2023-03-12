def matrix_exponentiation(a,b,n,mod):

    result = [[0]*n for _ in range(n)]
    
    #항등행렬을 만든다
    for i in range(n):
        
        result[i][i] = 1
    
    while b:
        
        if b & 1: #if b % 2 == 1:
            
            result = matrix_multiplication(result,a,n,mod)
        
        a = matrix_multiplication(a,a,n,mod)
        b >>= 1 #b //= 2
    
    return exp