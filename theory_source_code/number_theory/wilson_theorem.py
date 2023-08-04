#wilson's theorem
#if p is prime, (p-1)! == p-1 mod p

def factorial(a,b):
    
    result = 1
    
    for i in range(a,b):
        
        result *= i
        result %= p
    
    return result

n,p = map(int,input().split())

if n == p-1:
    
    answer = p-1

elif n > p - n:
    
    # n! * (n+1)(n+2)(n+3)...(p-1) == p-1 mod p
    # n! * [(n+1)(n+2)(n+3)...(p-2)] == 1 mod p
    
    # because (n+1)(n+2)(n+3)...(p-2) and p is coprime,
    # (n!) mod p == ([(n+1)(n+2)(n+3)...(p-2)])^(-1) mod p
    # by fermat's little theorem, 
    # ([(n+1)(n+2)(n+3)...(p-2)])^(-1) mod p == ([(n+1)(n+2)(n+3)...(p-2)])^(p-2) mod p     
    answer = factorial(n+1,p-1)
    
    answer = pow(answer,p-2,p)

else:
    
    answer = factorial(2,n+1)

print(answer)