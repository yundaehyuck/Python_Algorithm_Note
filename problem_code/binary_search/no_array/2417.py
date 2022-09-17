from sys import stdin

def binary_search(target,start,end):
    
    while start <= end:
        
        mid = (start+end)//2

        if mid**2 < target:
            
            start = mid+1
        
        else:
            
            if (mid-1)**2 < target:
                
                return mid
            
            else:
                
                end = mid-1
    
    return end

n = int(stdin.readline())

if n == 0:
    
    print(0)

else:

    print(binary_search(n,0,n))