import math
from sys import stdin

def get_prime_bitmask(n):
    
    result = [255]*((n+1)//8+1)

    result[0 >> 3] &= ~(1 << (0 & 7))
    result[1 >> 3] &= ~(1 << (1 & 7))

    for i in range(2,int((n+1)**(1/2))+1):
        
        if result[i >> 3] & (1 << (i & 7)):
            
            for j in range(i*i,n+1,i):
                
                result[j >> 3] &= ~(1 << (j & 7))
    
    return result

n = int(stdin.readline())

prime = get_prime_bitmask(n)

answer = 1

for i in range(2,n+1):
    
    if prime[i >> 3] & (1 << (i & 7)):
        
        answer *= pow(i,int(math.log(n,i)),2**32)
        answer %= (2**32)

print(answer)