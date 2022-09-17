def binary_search(target,start,end):
    
    while start <= end:
        
        mid = (start+end)//2

        if mid**3 == target:
            
            return mid
        
        elif mid**3 > target:
            
            end = mid-1
        
        else:
            
            start = mid+1
    
    return -1

T = int(input())

for t in range(1,T+1):
    
    target = int(input())

    print('#'+str(t),binary_search(target,0,target))