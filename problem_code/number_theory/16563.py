from sys import stdin

def get_spf(n):
    
    spf = [0]*(n+1)

    spf[1] = 1

    for i in range(2,n+1):
        
        spf[i] = i
    
    for i in range(4,n+1,2):
        
        spf[i] = 2
    
    for i in range(3,int((n+1)**(1/2))+1):
        
        if spf[i] == i:
            
            for j in range(i*i,n+1,i):
                
                if spf[j] == j:
                    
                    spf[j] = i
    
    return spf

def get_factorization(x,spf):
    
    factor = []

    while x != 1:
        
        factor.append(spf[x])

        x = x//spf[x]
    
    return factor

n = int(stdin.readline())

num = list(map(int,stdin.readline().split()))

spf = get_spf(5000000)

for k in num:
    
    print(*get_factorization(k,spf))
    
"""
#trivial solution
from sys import stdin

N = 5000000
sieve = [1]*(N+1)
primes = []

for p in range(2,int((N+1)**(1/2))+1):
    
    prime = True
    
    for i in range(2,int((p+1)**(1/2))+1):
        
        if p % i == 0:
            
            prime = False
            
            break
    
    if prime:
        
        primes.append(p)

def get_factorization(k,primes):
    
    factor = []
    
    for p in primes:
        
        if p*p > k:
            
            break
        
        while k % p == 0:
            
            k = k//p
            factor.append(p)
        
    
    if k > 1:
        
        factor.append(k)
    
    return factor


n = int(input())

num = list(map(int,input().split()))

for k in num:
    
    print(*get_factorization(k,primes))

"""