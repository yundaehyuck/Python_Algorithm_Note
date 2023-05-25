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

def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

mod = 1000000007

n,m = map(int,stdin.readline().split())

matrix = [[1,1],[1,0]]

#gcd(f_n,f_m) = f_(gcd(n,m))
x = gcd(n,m)

print(matrix_exponentiation(matrix,x,mod)[1][0])