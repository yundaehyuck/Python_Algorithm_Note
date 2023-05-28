from sys import stdin

def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

def lcm(a,b):
    
    return a*b//gcd(a,b)

d,m = map(int,stdin.readline().split())

D = list(map(int,stdin.readline().split()))

M = list(map(int,stdin.readline().split()))

#M에서 최대공약수를 구한다
gcd_m = M[0]

for i in range(1,m):
    
    gcd_m = gcd(gcd_m,M[i])

#최대공약수의 약수는, M의 모든 수들의 공약수이다.
divisor = set()

for i in range(1,int(gcd_m**(1/2))+1):
    
    if gcd_m % i == 0:
        
        divisor.add(i)
        divisor.add(gcd_m//i)

#D에서 최소공배수를 구한다
lcm_d = D[0]

for i in range(1,d):
    
    lcm_d = lcm(lcm_d,D[i])

#약수들이 최소공배수의 배수라면, 
#D의 모든 수들의 배수이면서 M의 모든 수들의 약수가 된다
count = 0

for div in divisor:

    if div % lcm_d == 0:
        
        count += 1
        
print(count)