"""
from sys import stdin

def factorization(n):
    
    p = 2

    cnt = [0]*(n+1)

    while p*p <= n:

        while n % p == 0:
            
            n = n//p

            cnt[p] += 1
        
        p += 1
    
    if n > 1:
        
        cnt[n] += 1
    
    return cnt

n = int(stdin.readline())

if n <= 1:
    
    print(0)

else:
    
    ans2 = 0
    ans5 = 0

    for i in range(2,n+1):
        
        cnt = factorization(i)

        if i >= 5:
            
            ans2 += cnt[2]
            ans5 += cnt[5]
        
        else:
            
            ans2 += cnt[2]
    
    print(min(ans2,ans5))"""

from sys import stdin

n = int(stdin.readline())

answer = 0

p = 5

while n >= p:
    
    x = n//p
    
    answer += x

    p *= 5
    
print(answer)