n = int(input())

ab_list = [0]*(n+1)

for a in range(1,int(n**(1/2))+1):
    
    for b in range(a,n):
        
        if a*b > n:
            
            break

        if a == b:
            
            ab_list[a*b] += 1
        
        else:
            
            ab_list[a*b] += 2

count = 0

for i in range(1,n):
    
    count += (ab_list[i] * ab_list[n-i])

print(count)