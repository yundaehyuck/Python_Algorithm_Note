#피보나치 수열의 합
from sys import stdin

def matrix_multiplication(a,b,mod):
    
    result = [[0,0],[0,0]]

    for i in range(2):
        
        for j in range(2):
            
            for k in range(2):
                
                result[i][j] += a[i][k]*b[k][j]
                result[i][j] %= mod
    
    return result

def matrix_exponentiation(matrix,n,mod):
    
    result = [[1,0],[0,1]]

    while n > 0:
        
        if n % 2 == 1:
            
            result = matrix_multiplication(result,matrix,mod)
        
        matrix = matrix_multiplication(matrix,matrix,mod)
        
        n //= 2
    
    return result

#피보나치 수열의 n번째 항까지의 합은, n+2번째 항에 1을 뺀 값과 같다.
mod = 1000000000

a,b = map(int,stdin.readline().split())

matrix = [[1,1],[1,0]]

sum_a = matrix_exponentiation(matrix,a+1,mod)

sum_b = matrix_exponentiation(matrix,b+2,mod)

print((sum_b[1][0] - sum_a[1][0] + mod) % mod)