#for n < 2**32
a_list = [2,7,61]

#modulo exponentiation

def power(x,y,m):
    
    result = 1

    x = x % m

    while y > 0:
        
        if y & 1:
            
            result *= x
            result %= m
        
        y = y >> 1
        x *= x
        x %= m
    
    return result

#miller_rabin test
def miller_rabin(n, a):
    
    d = n - 1

    while (d % 2 == 0):

        if power(a, d, n) == n-1:

            return True

        d = d >> 1

    temp = power(a, d, n)

    return temp == n-1 or temp == 1 #a^d = 1(mod n)인 경우

#primality test
def is_prime(n):

    if n <= 1:

        return False

    if n <= 10000: #n is very small
        
        for i in range(2,int((n+1)**(1/2))+1):
            
            if n % i == 0:
                
                return False
        
        return True
    
    for a in a_list:
        
        if miller_rabin(n,a) == False:
            
            return False
    
    return True


print(is_prime(13222123)) #True
print(is_prime(11221222)) #False

"""
#modulo exponentiation

def power(x,y,m):
    
    result = 1

    x = x % m

    while y > 0:
        
        if y & 1:
            
            result *= x
            result %= m
        
        y = y >> 1
        x *= x
        x %= m
    
    return result
    
def miller_rabin(n, a):
    
    d = n - 1

    while (d % 2 == 0):

        if power(a, d, n) == n-1:

            return True

        d = d >> 1

    temp = power(a, d, n)

    return temp == n-1 or temp == 1

def miller_rabin_test(n,a_list):
    
    for a in a_list:
        
        if miller_rabin(n,a) == False:
            
            return False
    
    return True

def is_prime(n):

    if n <= 1:

        return False

    if n <= 1000: #n is very small
        
        for i in range(2,int((n+1)**(1/2))+1):
            
            if n % i == 0:
                
                return False
        
        return True
    
    elif n < 2047:
        
        a_list = [2]
    
    elif n < 1373653:
        
        a_list = [2,3]
    
    elif n < 9080191:
        
        a_list = [31,73]
    
    elif n < 25326001:
        
        a_list = [2,3,5]
    
    elif n < 3215031751:
        
        a_list = [2,3,5,7]
    
    elif n < 4759123141:
        
        a_list = [2,7,61]
    
    elif n < 1122004669633:
        
        a_list = [2,13,23,1662803]
    
    elif n < 2152302898747:
        
        a_list = [2,3,5,7,11]
    
    elif n < 3474749660383:
        
        a_list = [2,3,5,7,11,13]
    
    elif n < 341550071728321:
        
        a_list = [2,3,5,7,11,13,17]
    
    elif n < 3825123056546413051:
        
        a_list = [2,3,5,7,11,13,17,19,23]
    
    elif n < 18446744073709551616:
        
        # n < 2**64
        
        #a_list = [2,3,5,7,11,13,17,19,23,29,31,37]

        a_list = [2,325,9375,28178,450775, 9780504, 1795265022]
    
    elif n < 318665857834031151167461:

        a_list = [2,3,5,7,11,13,17,19,23,29,31,37]
    
    elif n < 3317044064679887385961981:
        
        a_list = [2,3,5,7,11,13,17,19,23,29,31,37,41]

    return miller_rabin_test(n,a_list)
"""