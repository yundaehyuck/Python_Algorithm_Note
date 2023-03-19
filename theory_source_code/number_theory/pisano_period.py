from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    
    n,m = map(int,stdin.readline().split())

    a0,a1 = 0,1

    period = 1

    for _ in range(m*m):
        
        a0,a1 = a1,(a0+a1)%m

        if a0 == 0 and a1 == 1:
            
            print(n,period)
            break
        
        else:
            
            period += 1