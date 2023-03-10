n = int(input())
 
count1 = 0
count2 = 0
count = 0
 
for x in range(1,n):
    
    y = n-x
 
    for a in range(1,int(x**(1/2))+1):
        
        if x % a == 0:
            
            count1 += 1
 
            if x != a*a:
                
                count1 += 1
        
    
    for c in range(1,int(y**(1/2))+1):
        
        if y % c == 0:
            
            count2 += 1
 
            if y != c*c:
                
                count2 += 1
    
 
    count += (count1*count2)
    count1 = 0
    count2 = 0
 
print(count)