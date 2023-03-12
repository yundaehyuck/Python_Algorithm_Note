def matrix_multiplication(a,b,n,mod):

    mul = [[0] * n for _ in range(n)]

    for i in range(n):
        
        for j in range(n):
            
            for k in range(n):
                
                mul[i][j] += a[i][k] * b[k][j]

                mul[i][j] %= mod
    
    return mul