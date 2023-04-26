from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    
    n = int(stdin.readline())

    if n % 2 == 1:
        
        print(n*(n-1)*(n-2))
    
    else:
        
        if n % 3 == 0 and (n-3) % 3 == 0:
            
            print((n-1)*(n-2)*(n-3))
        
        else:
            
            print(n*(n-1)*(n-3))

"""
from sys import stdin

def gcd(a,b):
    
    while b != 0:
        a,b = b,a%b
    
    return a

def lcm(a,b):
    
    g = gcd(a,b)
    
    n = a//g
    m = b//g
    
    return g*n*m

t = int(stdin.readline())

for _ in range(t):
    
    n = int(stdin.readline())
        
    a = lcm(lcm(n-1,n-2),n-3)
    b = lcm(lcm(n,n-1),n-3)
    c = lcm(lcm(n,n-1),n-2)

    print(max(a,b,c))
"""