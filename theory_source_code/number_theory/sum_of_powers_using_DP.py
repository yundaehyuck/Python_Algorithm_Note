def mod_factorial(p,mod):
    
    factorial = [0]*(p+2)
    factorial[0] = 1

    for i in range(1,p+2):
    
        factorial[i] = factorial[i-1]*i
        factorial[i] %= mod
    
    return factorial

#(n)!*(n!)^(p-2) == 1
#(n-1)!*n*(n!)^(p-2) == 1
def mod_inv_factorial(factorial,p,mod):
    
    inverse = [0]*(p+2)

    inverse[p+1] = pow(factorial[p+1],mod-2,mod)

    for i in range(p+1,0,-1):
        
        inverse[i-1] = inverse[i]*i
        inverse[i-1] %= mod
    
    return inverse

#(n+1)^(p+1) - 1 = sigma(t=0)^(p) (p+1Ct)St(n)
#nCr = n!/(r!)*(n-r)!
def sum_of_power(factorial,inverse,n,p):
    
    S = [0]*(p+1)

    S[0] = n % mod

    for i in range(1,p+1):
        
        sigma = 0

        #sum(j = 0)^(i-1) (i+1)Cj*Sj(n)
        for j in range(i+1):
            
            sigma += (S[j] * factorial[i+1]*inverse[j]*inverse[i+1-j])
            sigma %= mod

        #Si(n) = ((n+1)^(i+1)-1 - sigma)*(i+1)Ci^(-1)

        S[i] = pow(n+1,i+1,mod) -1 - sigma
        
        S[i] %= mod

        #(i+1)C(i) = i+1
        S[i] *= pow(i+1,mod-2,mod)

        S[i] %= mod
    
    return S[p]

n,p = map(int,input().split())

mod = 10**9+7

factorial = mod_factorial(p,mod)
inverse = mod_inv_factorial(factorial,p,mod)

print(sum_of_power(factorial,inverse,n,p))