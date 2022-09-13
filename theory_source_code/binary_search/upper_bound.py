def upper_bound(array,target):

    n = len(array)
    
    #0~n에서 시작

    start,end = 0,n
    
    while start < end:
        
        mid = (start+end)//2

        if target < array[mid]:
            
            end = mid
        
        else:
            
            start = mid + 1

    
    #만약에 end가 음수라면, 찾지 못했다는 뜻입니다.

    if end < 0:
        
        return -1
    
    else: #그렇지 않다면 end-1을 array에 indexing해서 target과 일치하면
        
        if array[end-1] == target:
            
            return end-1 #end-1이 target의 위치이고
        
        else: #target과 다르다면 찾지 못했다는 뜻입니다.
            
            return -1