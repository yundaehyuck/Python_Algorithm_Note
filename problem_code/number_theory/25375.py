from sys import stdin

q = int(stdin.readline())

for _ in range(q):
    
    a,b = map(int,stdin.readline().split())

    if(b % a == 0):
        
        if b // a >= 2:
        
            print(1)
        
        else:
            
            print(0)
    
    else:
        
        print(0)