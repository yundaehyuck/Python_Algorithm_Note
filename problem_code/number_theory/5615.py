from sys import stdin

def miller_rabin(n, a):
    
    d = n - 1

    while d % 2 == 0:
        
        if pow(a,d,n) == n-1:
            
            return True
        
        d = d >> 1
    
    temp = pow(a,d,n)

    return temp == n-1 or temp == 1

def is_prime(n,a_list):
    
    if n <= 1:
        
        return False
    
    elif n <= 10000:
        
        for i in range(2,int((n+1)**(1/2))+1):
            
            if n % i == 0:
                
                return False
        
        return True
    
    else:
        
        for a in a_list:
            
            if miller_rabin(n,a) == False:
                
                return False
        
        return True

a_list = [2,7,61]

n = int(stdin.readline())

answer = 0

for _ in range(n):
    
    area = int(stdin.readline())

    p = 2*area+1

    answer += is_prime(p,a_list)

print(answer)