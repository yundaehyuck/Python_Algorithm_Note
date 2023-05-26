#1항부터 2n번째 항까지 짝수번째 피보나치 수열의 합
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
    
#1항부터 2n번째 항까지 합 2,4,6,8,...,2n번째 피보나치 합은 2n+1번째 항 - 1과 같다.

n = int(stdin.readline())//2

matrix = [[1,1],[1,0]]

result = matrix_exponentiation(matrix,2*n+1,mod)

print(result[1][0]-1)