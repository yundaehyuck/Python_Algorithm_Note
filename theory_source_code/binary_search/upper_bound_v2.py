def upper_bound(start,end,x):
    
    while (start != end):
        
        mid = start + (end - start)//2
        
        #mid가 x보다 크다면...
        #mid+1부터 end-1까지 모두 x보다 크므로...
        #x보다 큰 "첫번째 위치"는 mid+1 이후에는 존재하지 않고 [start,end]에 존재
        if mid > x:
            
            end = mid
        
        else:
            
            start = mid + 1
    
    return start