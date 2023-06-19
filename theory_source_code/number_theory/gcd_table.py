def get_prime(n):
    
    result = [1]*(n+1)

    for i in range(2,int((n+1)**(1/2))+1):
        
        if result[i] == 1:
            
            for j in range(i*i,n+1,i):
                
                result[j] = 0
    
    return [i for i in range(2,n+1) if result[i] == 1]

n,m = map(int,input().split())

if n > m:
    
    n,m = m,n

prime_list = get_prime(n)

answer = 1

mod = 1000000007

#gcd table에서 존재하는 모든 소수 p의 개수는..
#p의 개수 + p^2의 개수 + p^3의 개수 + ...

#p의 개수는 n//p*m//p개
for p in prime_list:
    
    x = p

    k = 0

    while n//x != 0:
        
        k += (n//x)*(m//x)

        x *= p
    
    answer *= pow(p,k,mod)
    answer %= mod
    
print(answer % mod)