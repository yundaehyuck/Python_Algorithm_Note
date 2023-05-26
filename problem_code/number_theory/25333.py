from sys import stdin

def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

T = int(stdin.readline())

for _ in range(T):
    
    a,b,x = map(int,stdin.readline().split())

    gcd_ab = gcd(a,b)

    print(x//gcd_ab)