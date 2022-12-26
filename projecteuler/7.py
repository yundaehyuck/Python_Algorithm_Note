def get_prime(n):
    
    result = [1]*(n+1)

    for i in range(2,int((n+1)**(1/2))+1):
        
        if result[i] == 1:
            
            for i in range(i+i,n+1,i):
                
                result[i] = 0
    
    return [i for i in range(2,n+1) if result[i] == 1]

print(get_prime(110000)[10000])