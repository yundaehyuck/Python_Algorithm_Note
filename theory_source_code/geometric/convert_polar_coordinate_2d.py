import math
from sys import stdin

def distance(x,y):
    
    return (x**2 + y**2)**(1/2)

def theta(x,y):
        
    t = math.atan2(y,x)

    if t < 0:

        return 2*math.pi+t

    else:

        return t

def convert(n,x,y):
    
    if n == 1:
        
        r = distance(x,y)

        if r == 0:
            
            return 0,0
        
        else:
            
            return r,theta(x,y)
    
    else:
            
        return x*math.cos(y),x*math.sin(y)

T = int(stdin.readline())

for _ in range(T):
    
    n = int(stdin.readline())

    x,y = map(float,stdin.readline().split())

    a,b = convert(n,x,y)

    print(a,b)