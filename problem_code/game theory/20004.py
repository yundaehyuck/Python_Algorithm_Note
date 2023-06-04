from sys import stdin

A = int(stdin.readline())

for n in range(1,A+1):
    
    x = 30 % (n+1)

    if x == 0:
        
        print(n)
