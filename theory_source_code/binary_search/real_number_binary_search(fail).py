#boj 14609
#이 방법은 일부 문제에서 안될 수 있다
from sys import stdin

def binary_search(a,b,n,real,k,c):
    
    delta = (b-a)/n

    start = 0
    end = delta

    while abs(start-end) > 10**(-5):
        
        approx = n*(c[-1])
        
        mid = start + (end - start)/2

        for j in range(1,k+1):
            
            for h in range(n):
            
                approx += (c[-(j+1)]*((a+h*delta+mid)**j))
        
        approx *= delta
            
        if real > approx:

            start = mid + 10**(-5)

        else:

            end = mid

    return end
        
k = int(stdin.readline())

c = list(map(int,stdin.readline().split()))

a,b,n = map(int,stdin.readline().split())

real = 0

for i in range(k+1):
    
    real += c[i]*(((b**(k+1-i))- (a**(k+1-i)))/(k+1-i))

print(binary_search(a,b,n,real,k,c))