from sys import stdin

s,m = map(int,stdin.readline().split())

ahri = (1<<10)-1

if s & ~(ahri) == 0:
    
    print('No thanks')

else:
    
    remain = s - ahri
    
    if remain & ~(m) == 0:
        
        print('Thanks')
    
    else:
        
        print('Impossible')