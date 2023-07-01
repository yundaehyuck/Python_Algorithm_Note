#n! mod p = ((p-1)! mod p)^(n//p) * (n mod p)! * p^e mod p

#if p is prime, (p-1)! mod p = -1
#Legendre's formula, we can compute e
n,p = map(int,input().split())

result = (-1)**(n//p)

for i in range(1,n%p+1):
    
    result *= i
    result %= p

count = 0
x = p

while n//x > 0:
    
    count += n//x
    x *= p

print(result * pow(p,count,p) % p)