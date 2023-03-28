#x보다 크거나 같은 첫번째 위치를 찾는 함수
def lower_bound(start,end,x):
    
    while(start != end):
        
        mid = start + (end-start)//2
        
        #mid+1~end-1까지는 모두 x이상이므로...
        #x보다 크거나 같은 첫번째 위치는 [start,mid)에 존재한다.
        if mid >= x:
            
            end = mid
        
        else:
            
            start = mid + 1
    
    return start