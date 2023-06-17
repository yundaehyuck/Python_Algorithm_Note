import math
from sys import stdin

def divisor(n):
    
    result = []
    
    for i in range(1,int(n**(1/2))+1):
        
        if n % i == 0:
            
            if n//i == i:

                result.append(i)

            else:

                result.append(i)
                result.append(n//i)

    return result 

a,b = map(int,stdin.readline().split())

if a > b:
    
    a,b = b,a

x = b-a

if x == 0:
    
    print(1)

else:

    i = math.ceil(b/x)

    if x*i == b:
        
        i += 1

    n1 = x*i-b
    min_lcm = (a+n1)*(b+n1)//x

    d = divisor(x)

    for i in d:
        
        n = i - a

        if n > 0:
            
            if b+n < min_lcm:
                
                n1 = n
                min_lcm = b+n
    print(n1)