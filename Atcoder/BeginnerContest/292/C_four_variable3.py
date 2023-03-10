def prime_factorization(n):
    
    answer = 1

    p = 2

    count = 0

    while p*p <= n:
        
        while n % p == 0:
            
            n = n // p
            count += 1
        
        p += 1
        answer *= (count+1)
        count = 0
    
    if n > 1:
        
        answer *= 2
    
    return answer

n = int(input())

count1 = 0
count2 = 0
count = 0

for x in range(1,n):
    
    y = n-x

    count1 = prime_factorization(x)
    count2 = prime_factorization(y)
    
    count += (count1*count2)
    count1 = 0
    count2 = 0

print(count)