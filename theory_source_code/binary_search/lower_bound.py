def lower_bound(array,target):
    
    n = len(array)
    
    ##0~n에서 탐색 시작

    start,end = 0,n
    
    while start < end:
        
        mid = (start+end)//2

        if target <= array[mid]:
            
            end = mid
        
        else:
            
            start = mid + 1

    
    #최종 위치가 n이라면 탐색하지 못했다는 뜻입니다.

    if end == n:
        
        return -1
    
    else: #end가 n이 아닌 경우에
        
        if array[end] == target: #실제 array값이 target과 같다면 찾았다는 뜻이고
        
            return end
        
        else: #그렇지 않다면 못찾았다는 뜻입니다.
            
            return -1