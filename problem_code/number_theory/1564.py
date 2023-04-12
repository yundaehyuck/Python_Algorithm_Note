from sys import stdin

n = int(stdin.readline())

prod = 1

for i in range(1,n+1):
    
    prod *= i
    
    while prod % 10 == 0:
        
        prod //= 10
    
    prod %= 10**13

x = (prod % (10**5))

print('0'*(5-len(str(x)))+str(x))