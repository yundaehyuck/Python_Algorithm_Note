#two pointer
from sys import stdin

def is_prime(n):
    
    if n == 1:
        
        return False
    
    else:
        
        for i in range(2,int(n**(1/2))+1):
            
            if n % i == 0:
                
                return False
        
        return True

def goldbach(m):
    
    k = m//2

    for i in range(k):
        
        if is_prime(k-i) and is_prime(k+i):
            
            return [k-i,k+i]

n = int(stdin.readline())

if n < 8:
    
    print(-1)

else:
    
    if n % 2 == 0:
        
        n -= 4

        answer = goldbach(n)

        answer.append(2)
        answer.append(2)

    
    else:
        
        n -= 5

        answer = goldbach(n)

        answer.append(2)
        answer.append(3)
    
    print(*answer)


""" second for loop
from sys import stdin

def get_prime(n):
    
    result = [1]*(n)

    for i in range(2,int((n)**(1/2))+1):
        
        for j in range(i+i,n,i):
            
            if result[i] == 1:
                
                result[j] = 0
    
    return [i for i in range(2,n) if result[i] == 1]

n = int(stdin.readline())

if n < 8:
    
    print(-1)

else:

    if n % 2 == 0:
        
        n -= 4

        answer = [2,2]
    
    else:
        
        n -= 5

        answer = [2,3]

    prime_list = get_prime(n)

    p = len(prime_list)

    find = False

    for a in range(p):
        
        for b in range(a,p):

            if prime_list[a] + prime_list[b] == n:

                find = True

                answer.append(prime_list[a])
                answer.append(prime_list[b])

                break

        if find:

            break
    
    if find:
        
        print(*answer)
    
    else:
        
        print(-1)
"""


""" #brute force 4 forloop
from sys import stdin

def get_prime(n):
    
    result = [1]*(n+1)

    for i in range(2,int((n+1)**(1/2))+1):
        
        for j in range(i+i,n+1,i):
            
            if result[i] == 1:
                
                result[j] = 0
    
    return [i for i in range(2,n+1) if result[i] == 1]

n = int(stdin.readline())

prime_list = get_prime(n)

p = len(prime_list)

find = False

for a in range(p):
    
    for b in range(a,p):
        
        for c in range(b,p):
            
            for d in range(c,p):
                
                if prime_list[a]+prime_list[b]+prime_list[c]+prime_list[d] == n:
                    
                    find = True
                    break
            
            if find:
                
                break
        
        if find:
            
            break
    
    if find:
        
        break

if find == False:
    
    print(-1)

else:

    answer = [prime_list[a],prime_list[b],prime_list[c],prime_list[d]]

    answer.sort()

    print(*answer)
"""


