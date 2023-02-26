from sys import stdin

def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

a,d = map(int,stdin.readline().split())

q = int(stdin.readline())

for _ in range(q):
    
    c,l,r = map(int,stdin.readline().split())

    if c == 1:

        print((r-l+1)*(a+(l-1)*d + a+(r-1)*d)//2)
    
    else:
        
        if l == r:
            
            print(a+(l-1)*d)
        
        else:
            
            g = gcd(a,d)

            print(g)