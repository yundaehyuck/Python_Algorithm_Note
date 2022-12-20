def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

lcm = (1*2)//gcd(1,2)

for n in range(3,21):
    
    lcm = (lcm*n)//gcd(lcm,n)

print(lcm)