from sys import stdin

def matrix_multiplication(a,b,mod):
    
    result = [[0,0],[0,0]]

    for i in range(2):
        
        for j in range(2):
            
            for k in range(2):
                
                result[i][j] += a[i][k]*b[k][j]

                result[i][j] %= mod
    
    return result

def matrix_exponentiation(m,n,mod):
    
    result = [[1,0],[0,1]]

    while n > 0:
        
        if n % 2 == 1:
            
            result = matrix_multiplication(result,m,mod)
        
        m = matrix_multiplication(m,m,mod)
        n //= 2
    
    return result

n = int(stdin.readline())

matrix = [[1,1],[1,0]]

mod = 1000000007

result = matrix_exponentiation(matrix,n,mod)

print(result[1][0])