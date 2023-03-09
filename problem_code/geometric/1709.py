from sys import stdin

n = int(stdin.readline())

n = n//2
r2 = (n)**2

count = 0
start = 0

for y in range(n-1,-1,-1):
    
    for x in range(start,n):
        
        down = x**2+y**2
        up = (x+1)**2+(y+1)**2

        if r2 > down and r2 < up:
            
            count += 1
        
        elif down >= r2:
            
            start = x-1
            break

print(count*4)