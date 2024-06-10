def f(k):
    
    if k == 0:
        
        return ["#"]
    
    sub = f(k-1)
    
    l = len(sub)
    
    pattern = [["." for _ in range(3*l)] for _ in range(3*l)]
    
    for I in range(3):
        
        for J in range(3):
            
            if I != 1 or J != 1:
                
                for i in range(l):
                    
                    for j in range(l):
                        
                        pattern[i+I*l][j+J*l] = sub[i][j]
    
    
    return pattern

k = int(input())

pattern = f(k)

for row in pattern:

    print("".join(row))