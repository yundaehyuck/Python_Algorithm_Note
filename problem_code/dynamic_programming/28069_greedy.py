n,k = map(int,input().split())

for _ in range(k):
    
    x1 = n-1

    if n % 3 == 0:
        
        x2 = 2*n//3
    
    elif (2*n+1) % 3 == 0:
        
        x2 = (2*n+1)//3
    
    else:
        
        x2 = n-1
    
    n = min(x1,x2)
    
    if n == 0:
        
        print("minigimbob")
        break

if n != 0:
    
    print("water")