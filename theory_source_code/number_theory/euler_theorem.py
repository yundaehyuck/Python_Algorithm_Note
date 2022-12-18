from sys import stdin

def phi(n):
    
    result = n

    p = 2

    while p*p <= n:
        
        if n % p == 0:
            
            while n % p == 0:
                
                n = n//p
            
            result -= result // p
        
        p += 1
    
    if n > 1:
        
        result -= result // n
    
    return result
    
T = int(stdin.readline())

for t in range(1,T+1):
    
    a,n,p = map(int,stdin.readline().split())

    phi_p = phi(p)

    n_factorial = 1

    big = False

    for i in range(1,n+1):
        
        n_factorial *= i

        #n!을 구하는 와중에 n! >= phi(p)라면...

        if n_factorial >= phi_p:
            
            big = True

            n_factorial %= phi_p
    
    #n! >= phi(p)라면.. phi_p를 더해줘야함
    if big:
        
        n_factorial += phi_p
    
    print(f'Case #{t}: {pow(a,n_factorial,p)}')