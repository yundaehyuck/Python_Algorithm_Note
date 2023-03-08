from sys import stdin

def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

G,L = map(int,stdin.readline().split())

x = L//G

for i in range(1,int(x**(1/2))+1):

    if x % i == 0 and gcd(i,x//i) == 1:

        answer = i

print(G*answer, G*(x//answer))