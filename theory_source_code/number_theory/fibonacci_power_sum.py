#피보나치 수열 각 항의 제곱의 합
from sys import stdin

mod = 1000000007

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

#피보나치 수열의 n번째 항까지 제곱의 합은, n번째 항과 n+1번째 항의 곱과 같다
n = int(stdin.readline())

matrix = [[1,1],[1,0]]

result = matrix_exponentiation(matrix,n,mod)

#(0,0)이 n+1번째 항, (1,0)이 n번째 항이다
print((result[0][0]*result[1][0])%mod)