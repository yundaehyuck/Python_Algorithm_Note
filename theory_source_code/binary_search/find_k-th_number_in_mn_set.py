#BOJ 1300
def lower_bound(target,start,end,n):
    
    while start < end:
        
        mid = (start+end)//2

        sum = 0
        
        #A의 각 행에서 mid보다 작거나 같은 수의 개수를 세준다.
        for i in range(1,n+1):
            
            #길이가 n인 각 행에서 mid보다 작거나 같은 수의 개수는 최대 n개이다.
            sum += min(mid//i, n)
        
        #크면 클수록, 해당 수보다 작거나 같은 수의 개수는 증가하니까...
        
        #mid보다 작거나 같은 수의 개수가 target값보다 크거나 같다면, 
        #찾고자 하는 값은 mid보다 작거나 같다.
        if sum >= target:
            
            end = mid
        
        #mid보다 작거나 같은 수의 개수가 target보다 작다면..
        #찾고자 하는 값은 mid보다 클것이다.
        else:
            
            start = mid+1
        
    return end

