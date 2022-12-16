from sys import stdin

def extended_gcd(a,b):
    
    before_x = 1
    before_y = 0

    x = 0
    y = 1

    while b != 0:
        
        q,r = a//b, a%b

        a,b = b,r

        before_x,x = x,before_x - x*q
        before_y,y = y,before_y - y*q
    
    return a,before_x,before_y

n,a = map(int,stdin.readline().split())

gcd,c,y = extended_gcd(a,n)

#곱셈에 대한 역원
if gcd == 1:
    
    if c < 0:
        
        while c < 0:
            
            c += n
        
    
    if c > n-1:
            
        c = -1

else:
    
    c = -1

#덧셈에 대한 역원은 n-a
print(n-a,c)