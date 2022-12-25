#https://www.acmicpc.net/problem/11693

from sys import stdin

#1+r+r**2+...+r**n의 합
def geometric(r,n,mod):

    if n == 0:
        
        return 1
    
    else:

        if n % 2 == 1:
            
            return ((1+r)*geometric(r*r%mod,(n-1)//2,mod))%mod
        
        elif n % 2 == 0:
            
            return 1+((r+r*r)%mod*geometric(r*r%mod,(n-2)//2,mod))%mod

n,m = map(int,stdin.readline().split())

mod = 1000000007

#n에 대한 소인수분해
prime = []

p = 2

while p*p <= n:
    
    if n % p == 0:
        
        count = 0

        while n % p == 0:
            
            n = n//p

            count += 1
        
        prime.append((p,count*m))
    
    p = p + 1

if n > 1:
    
    prime.append((n,m))

answer = 1

#약수의 합
#초항이 1이고, 항 수가 count+1이고 공비가 소인수 p인 등비수열의 합의 곱이 약수의 합
for p,count in prime:
    
    answer *= geometric(p,count,mod)

    answer %= mod

print(answer)