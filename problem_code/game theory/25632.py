from sys import stdin

def get_prime(a,b):
    
    result = []
    count = 0
    
    for n in range(a,b+1):
        
        prime = True

        for i in range(2,int((n+1)**(1/2))+1):
            
            if n % i == 0:
                
                prime = False
                break
        
        if prime:
            
            result.append(n)
            count += 1
    
    return result,count

a,b = map(int,stdin.readline().split())

c,d = map(int,stdin.readline().split())

yt,p = get_prime(a,b)
yj,q = get_prime(c,d)

common = []
r = 0

for n in yt:
    
    if n in yj:
        
        common.append(n)
        r += 1

if p > q:
    
    print('yt')

elif p < q:
    
    print('yj')

else:

    if r % 2 == 1:
        
        print('yt')
    
    else:
        
        print('yj')