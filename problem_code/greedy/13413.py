from sys import stdin

T = int(stdin.readline())

for _ in range(T):

    n = int(stdin.readline())

    s = stdin.readline()
    t = stdin.readline()
    
    W = 0
    B = 0

    for i in range(n):
        
        if s[i] != t[i]:
            
            if s[i] == 'W':
                
                W += 1
            
            else:
                
                B += 1
    
    if W >= B:
        
        print(W)
    
    else:
        
        print(B)